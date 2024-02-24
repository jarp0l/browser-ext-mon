HTTP_SERVER_USE_ENROLL_SECRET = True
HTTP_SERVER_ENROLL_SECRET = "test_enroll_secret.txt"

EXAMPLE_CONFIG = {
    "options": {
        "host_identifier": "uuid",
    },
    "schedule": {
        "ff_addons": {
            "query": "select identifier, source_url name from firefox_addons where source_url<>'null' limit 2;",
            "interval": 5,
        },
    },
    "log_type": "result",
    "node_invalid": False,
}

# A 'node' variation of the TLS API uses a GET for config.
EXAMPLE_NODE_CONFIG = EXAMPLE_CONFIG
EXAMPLE_NODE_CONFIG["node"] = True

EXAMPLE_DISTRIBUTED = {
    "queries": {
        "info": "select count(1) from osquery_info",
        "flags": "select count(1) from osquery_flags",
    }
}

EXAMPLE_DISTRIBUTED_DISCOVERY = {
    "queries": {
        "windows_info": "select * from system_info",
        "darwin_chrome_ex": "select users.username, ce.* from users join chrome_extensions ce using (uid)",
    },
    "discovery": {
        "windows_info": "select * from os_version where platform='windows'",
        "darwin_chrome_ex": "select * from os_version where platform='darwin'",
    },
}

EXAMPLE_DISTRIBUTED_ACCELERATE = {
    "queries": {
        "info": "select * from osquery_info",
    },
    "accelerate": "60",
}


TEST_GET_RESPONSE = {
    "foo": "baz",
    "config": "baz",
}

TEST_POST_RESPONSE = {
    "foo": "bar",
}

NODE_KEYS = [
    "this_is_a_node_secret",
    "this_is_also_a_node_secret",
]

FAILED_ENROLL_RESPONSE = {"node_invalid": True}

ENROLL_RESPONSE = {"node_key": "this_is_a_node_secret"}

ENROLL_RESET = {
    "count": 1,
    "max": 3,
}
