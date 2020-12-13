def mock_generate_dataset():    
    cisco_valid_dataset= {"vendor": "cisco.com"}
    cisco_valid_dataset["url"] = "https://www.cisco.com/c/en/us/support/routers/910-industrial-router/model.html"
    cisco_valid_dataset["series"] = "Cisco 900 Series Industrial Routers"
    cisco_valid_dataset["category"] = "Routers"
    cisco_valid_dataset["model"] = "Cisco 910 Industrial Router"
    cisco_valid_dataset["path"] = "/Support/Product Support/Routers/Cisco 900 Series Industrial Routers"
    cisco_valid_dataset["release"] = 1404766800
    cisco_valid_dataset["endofsale"] = 1473886800
    cisco_valid_dataset["endofsupport"] = 1645998200
    cisco_valid_dataset["downloads"] = [
                                        {
                                            "latest": "1.2.1RB4",
                                            "filename": "firmware_P2MB_1.2.1rb4.zip",
                                            "size": 32406078,
                                            "md5": "a81300ffccbceff4f714c99c3ca3a12b"
                                        },
                                        {
                                            "all": "https://software.cisco.com/download/home/286277668/type/286277896/release/1.2.1RB4?i=!pp"
                                        }
                                        ]
    return cisco_valid_dataset

def mock_generate_invalid_path_dataset(invalid_path):    
    cisco_invalid_path_dataset= {"vendor": "cisco.com"}
    cisco_invalid_path_dataset["url"] = "https://www.cisco.com/c/en/us/support/routers/910-industrial-router/model.html"
    cisco_invalid_path_dataset["series"] = "Cisco 900 Series Industrial Routers"
    cisco_invalid_path_dataset["category"] = "Routers"
    cisco_invalid_path_dataset["model"] = "Cisco 910 Industrial Router"
    cisco_invalid_path_dataset["path"] = invalid_path
    cisco_invalid_path_dataset["release"] = 1404766800
    cisco_invalid_path_dataset["endofsale"] = 1473886800
    cisco_invalid_path_dataset["endofsupport"] = 1645998200
    cisco_invalid_path_dataset["downloads"] = [
                                        {
                                            "latest": "1.2.1RB4",
                                            "filename": "firmware_P2MB_1.2.1rb4.zip",
                                            "size": 32406078,
                                            "md5": "a81300ffccbceff4f714c99c3ca3a12b"
                                        },
                                        {
                                            "all": "https://software.cisco.com/download/home/286277668/type/286277896/release/1.2.1RB4?i=!pp"
                                        }
                                        ]
    return cisco_invalid_path_dataset

def generate_custom_dataset(vendor,url,series,category,model,path,release):
    cisco_dataset= {"vendor": vendor}
    cisco_dataset["url"] = url
    cisco_dataset["series"] = series
    cisco_dataset["category"] = category
    cisco_dataset["model"] = model
    cisco_dataset["path"] = path
    cisco_dataset["release"] = release
    cisco_dataset["endofsale"] = 1473886800
    cisco_dataset["endofsupport"] = 1645998200
    cisco_dataset["downloads"] = [
                                {
                                    "latest": "1.2.1RB4",
                                    "filename": "firmware_P2MB_1.2.1rb4.zip",
                                    "size": 32406078,
                                    "md5": "a81300ffccbceff4f714c99c3ca3a12b"
                                },
                                {
                                    "all": "https://software.cisco.com/download/home/286277668/type/286277896/release/1.2.1RB4?i=!pp"
                                }
                                ]
    return cisco_dataset