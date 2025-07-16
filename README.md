# TikTok Business API SDK

[![License](https://img.shields.io/badge/License-Tiktok%20-blue.svg?style=flat-square)](https://github.com/tiktok/tiktok-business-api-sdk/edit/main/LICENSE.md)

# Introduction
The [TikTok Business API SDK](https://ads.tiktok.com/marketing_api/docs?id=1764231376750658&rid=542rk6sm9jl) is a 
comprehensive suite of client libraries that can help our developers and partners to integrate with [TikTok API for Business](https://ads.tiktok.com/marketing_api/) 
easily and faster in a standardized way. It is the ultimate solution for developers looking to streamline the integration process and enhance productivity. 
Our SDK, launching in phases, includes APIs for Authentication, Campaign Creation, Reporting, Business Center and more.
For details, please refer to [this page](https://ads.tiktok.com/marketing_api/docs?id=1764231376750658&rid=542rk6sm9jl).

## Quick Start
Java, Python and Javascript are among the most popular languages for TikTok business third-party developers. The TikTok Business API SDK is a code package that provides an interface between your application and Tiktok's business APIs for these three languages. This tutorial provides the basic knowledge needed to access to our SDK and includes sample code for your reference.

## Version

- API version: 1.0.1 

## Prerequisites
  1.   [Create a TikTok For Business account](https://ads.tiktok.com/marketing_api/docs?id=1738855099573250)
  2.   [Register as a developer](https://ads.tiktok.com/marketing_api/docs?id=1738855176671234)
  3.   [Create a developer app](https://ads.tiktok.com/marketing_api/docs?id=1738855242728450)
  4.   [Obtain authorization](https://ads.tiktok.com/marketing_api/docs?id=1738373141733378)
  5.   [Obtain authentication](https://ads.tiktok.com/marketing_api/docs?id=1738373164380162)


## Integration with Python SDK

#### Version requirements

  - Python 3.4+

#### Integration Steps:
Option 1(recommended)
1. Download the TikTok Business API SDK within your project
   ```
    pip install tiktok-business-api-sdk-official
   ```
2. Import and use Python SDK method, below is the sample code for reference
   ```
    from __future__ import print_function
    import business_api_client
    from business_api_client.rest import ApiException
    from pprint import pprint

    def test_tool_language():
    # create an instance of the API class
        api_instance = business_api_client.ToolApi()
        advertiser_id = TEST_ADVERTISER_ID # str |
        access_token = TEST_ACCESS_TOKEN # str |

        try:
            api_response = api_instance.tool_language(advertiser_id, access_token)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ToolApi->tool_language: %s\n" % e)


    test_tool_language()
   ```
Option 2
1. Download the TikTok Business API SDK
   ```
    git clone https://github.com/tiktok/tiktok-business-api-sdk.git
   ```
2. Set up the Python virtual environment by using the following command. If you already have your own virtual environment, please skip this step and source into your own project.
   ```
    python3 -m venv your_virtual_env
    source your_virtual_env/bin/activate
   ```
3. Set Local env and install dependency with following commands
   ```
   export PYTHONPATH=your_path/tiktok-business-api-sdk:your_path/tiktok-business-api-sdk/python_sdk:your_path/tiktok-business-api-sdk/python_sdk/business_api_client
   cd your_path/tiktok-business-api-sdk/python_sdk
   pip install -r requirements.txt
   python3 setup.py install
   ```
4. Run and test the Python SDK. Below are the sample codes for your reference.
   ```
    from __future__ import print_function
    import business_api_client
    from pprint import pprint

    TEST_ADVERTISER_ID = 'Your_advertiser_id'
    TEST_ACCESS_TOKEN = 'Your_access_token'


    def test_tool_language():
    # create an instance of the API class
        api_instance = business_api_client.ToolApi()
        advertiser_id = TEST_ADVERTISER_ID # str |
        access_token = TEST_ACCESS_TOKEN # str |

        try:
            api_response = api_instance.tool_language(advertiser_id, access_token)
            pprint(api_response)
        except ApiException as e:
            print("Exception when calling ToolApi->tool_language: %s\n" % e)
   ```
5. Sample Code for Aco and Campaign Creation for reference

   ```
    from __future__ import print_function
    import business_api_client
    from business_api_client.rest import ApiException

    # Create instances of API classes
    campaign_instance = business_api_client.CampaignCreationApi()
    ad_aco_instance = business_api_client.AdAcoApi()

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"  # Replace with actual access token
    ADVERTISER_ID = "YOUR_ADVERTISER_ID"  # Replace with actual advertiser ID
    ADGROUP_ID = "YOUR_ADGROUP_ID"  # Replace with actual adgroup ID

    def create_campaign_and_aco_ad():
       # Create Campaign
       campaign_body = business_api_client.CampaignCreateBody(
          advertiser_id=ADVERTISER_ID,
          campaign_name="SDK-Campaign",
          objective_type="APP_PROMOTION",
          budget=50.0,
          budget_mode="BUDGET_MODE_TOTAL",
          app_promotion_type="APP_INSTALL"
       )

       try:
          campaign_response = campaign_instance.campaign_create(ACCESS_TOKEN, body=campaign_body)
          print("Campaign Created:", campaign_response)
          campaign_id = campaign_response["data"]["campaign_id"]
       except ApiException as e:
          print("Exception when calling CampaignCreationApi->campaign_create:", e)

       # Create ACO Ad
       common_material = business_api_client.AdAcoBodyCommonMaterial(
          creative_authorized=True,
          call_to_action_id="CALL_TO_ACTION_ID",
          identity_type="CUSTOMIZED_USER",
          identity_id="IDENTITY_ID",
       )

       media_info = business_api_client.AdAcoBodyMediaInfo(
          image_info=[business_api_client.AdAcoBodyMediaInfoImageInfo(web_uri="IMAGE_URI")],
          video_info=business_api_client.AdAcoBodyMediaInfoVideoInfo(
                video_id="VIDEO_ID", file_name="VIDEO_FILE_NAME"
          ),
       )

       media_info_list = [business_api_client.AdAcoBodyMediaInfoList(media_info=media_info)]

       title_list = [business_api_client.AdAcoBodyTitleList(title="Sample Title")]
       display_name_list = [business_api_client.AdAcoBodyDisplayNameList(app_name="Sample App")]
       deeplink_list = [
          business_api_client.AdAcoBodyDeeplinkList(deeplink="https://www.example.com", deeplink_type="NORMAL")
       ]

       body = business_api_client.AdAcoBody(
          advertiser_id=ADVERTISER_ID,
          adgroup_id=ADGROUP_ID,
          common_material=common_material,
          media_info_list=media_info_list,
          title_list=title_list,
          display_name_list=display_name_list,
          deeplink_list=deeplink_list,
       )

       try:
          response = ad_aco_instance.ad_aco_create(ACCESS_TOKEN, body=body)
          print("Ad ACO Created Successfully:", response)
       except ApiException as e:
          print("Exception when calling AdAcoApi->ad_aco_create:", e)


    create_campaign_and_aco_ad()
   ```
  


   ```
   
## Give feedback

- If you want to report bugs or issues, please visit [TikTok API for Business Developer Portal](https://ads.tiktok.com/marketing_api/homepage) and click "?"  on the top 
right to submit a ticket under Marketing API category.

## References

Here are the detailed documentation for currently supported programming languages.

- Python:  please refer to [python_sdk/README.md](https://github.com/tiktok/tiktok-business-api-sdk/blob/main/python_sdk/README.md)



