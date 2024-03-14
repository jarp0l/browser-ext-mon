import streamlit as st
import pandas as pd

from streamlit_app.utils.apis import get_nodes, make_get_request,get_extensions
from streamlit_app.utils.auth_form import LoginForm, auth_form

NUMBER_OF_NODES = None


def populate_node_page():
    org_id = "72b53p7ai8s9wdm"
    data_node = make_get_request(collection="nodes", filter=f"(org_id='{org_id}')")
    if data_node is None:
        st.error("error fetching nodes records")
        return
    return data_node


def populate_page():
    # hardcoded values for testing
    admin_email = "admin@admin.com"

    ## TO LIST THE ORGANIZATION DATA
    data_org = make_get_request(
        collection="organizations", filter=f"(admin_email='{admin_email}')"
    )

    if data_org is None:
        st.error("error fetching records ")
        return
    item_org = data_org["items"]
    api_keys = [org["api_key"] for org in item_org]

    ##  TO LIST THE NODES DATA
    org_id = "72b53p7ai8s9wdm"
    data_node = make_get_request(collection="nodes", filter=f"(org_id='{org_id}')")
    data_node = populate_node_page()
    NUMBER_OF_NODES = data_node["totalItems"]

   
    
    
    org_id = "72b53p7ai8s9wdm"
    data_node = get_nodes(org_id)

    item_node = data_node["items"]
    
   
   # top 5 most used extensions but using another api call 

    # for item in item_node:
    #     extension_firefox_node = get_extensions("firefox_extensions", item.get("id"))
    #     if extension_firefox_node is None:
    #         st.error("error fetching extension records")
    #         return
    #     if extension_firefox_node["totalItems"]:
    #         df = pd.DataFrame(extension_firefox_node["items"])
           
    #     else:
    #         st.error("total items in node is zero")

    

  
   
    # all_extensions = df["identifier"].value_counts().reset_index()
    # all_extensions.columns = ["identifier", "count"]
    # top_5_extensions = all_extensions.head(5)
    # st.subheader("Top 5 Most Used Extensions")
    # st.bar_chart(top_5_extensions.set_index("identifier"))
    
    col1, col2 = st.columns(2)

    with col1:
         # Use the new class
        st.write(f"Number of Nodes")
        st.write(f"{NUMBER_OF_NODES}")   

    with col2:
        # Use the new class
        st.write(f"API Key")
        st.write(f"{api_keys}")

    ## TO LIST THE EXTENSIONS DATA AND TOTAL ITEMS


def build_page():
    st.set_page_config(page_title="Dashboard")
    st.header("Dashboard")
    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


def main():
    if not LoginForm().is_logged_in():
        auth_form()
    else:
        build_page()


if __name__ == "__main__":
    main()
