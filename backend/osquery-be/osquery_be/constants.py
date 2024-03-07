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

ENROLL_RESET = {
    "count": 1,
    "max": 3,
}
