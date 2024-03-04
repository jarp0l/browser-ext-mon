package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/s3"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var bucketName = "bem-pb"

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		bucket, err := s3.NewBucket(ctx, bucketName, nil)
		if err != nil {
			return err
		}

		user, err := iam.NewUser(ctx, bucketName+"-user", nil)
		if err != nil {
			return err
		}

		accessKey, err := iam.NewAccessKey(ctx, bucketName+"-accessKey", &iam.AccessKeyArgs{
			User: user.Name,
		})
		if err != nil {
			return err
		}

		group, err := iam.NewGroup(ctx, bucketName+"-group", nil)
		if err != nil {
			return err
		}

		bucketPolicyOutput := bucket.Arn.ApplyT(func(arn string) (string, error) {
			policy := `{
				"Version": "2012-10-17",
				"Statement": [{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": "` + arn + `/*"
				}]
			}`
			return policy, nil
		}).(pulumi.StringOutput)

		bucketPolicy, err := iam.NewPolicy(ctx, bucketName+"-policy", &iam.PolicyArgs{
			Policy: bucketPolicyOutput,
		})
		if err != nil {
			return err
		}

		_, err = iam.NewGroupPolicyAttachment(ctx, bucketName+"-group-policy-attach", &iam.GroupPolicyAttachmentArgs{
			Group:     group.Name,
			PolicyArn: bucketPolicy.Arn,
		})
		if err != nil {
			return err
		}

		_, err = iam.NewGroupMembership(ctx, bucketName+"-user-membership", &iam.GroupMembershipArgs{
			Group: group.Name,
			Users: pulumi.StringArray{
				user.Name,
			},
		})
		if err != nil {
			return err
		}

		ctx.Export("bucketName", bucket.Bucket)
		ctx.Export("bucketArn", bucket.Arn)
		ctx.Export("accessKey", accessKey.ID())
		ctx.Export("secretKey", accessKey.Secret)
		return nil
	})
}
