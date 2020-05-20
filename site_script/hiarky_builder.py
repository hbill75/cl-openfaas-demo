#!/usr/bin/env python

"""
Copyright (c) 2019 Cisco and/or its affiliates.

This software is licensed to you under the terms of the Cisco Sample
Code License, Version 1.0 (the "License"). You may obtain a copy of the
License at

               https://developer.cisco.com/docs/licenses

All use of the material herein must be in accordance with the terms of
the License. All rights not expressly granted by the License are
reserved. Unless required by applicable law or agreed to separately in
writing, software distributed under the License is distributed on an "AS
IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
or implied.
"""

from dnacApi import apisvcs
import json
import time


USERNAME = "stevehi"
PASSWORD = "C1sco12345"
HOSTNAME = "10.86.85.168"

"""
Reads in the location details used to build the site hiearchy from
the locations_details.json file
"""

file_contents = open("location_details_1_site.json").read()
site_data = json.loads(file_contents)


if __name__ == "__main__":

    """
    Get the DNA Center x-auth-token using the argparse
    arguments
    """

    dnacAuth = apisvcs.auth_token(USERNAME, PASSWORD, HOSTNAME)


    print(" ")
    print("Starting DNAC site creation process...")
    print(" ")

    for site_details in site_data["locations"]:

            floor = site_details["floors"][0]
            newArea = apisvcs.site_build("area", 
                                          site_details["city"], 
                                          site_details["bldg"],
                                          site_details["address"], 
                                          str(floor), 
                                          site_details["latitude"],
                                          site_details["longitude"],
                                          site_details["width"],
                                          site_details["length"],
                                          site_details["heigth"],
                                          HOSTNAME, 
                                          dnacAuth["Token"])

            area_execution_success = json.loads(newArea.text)
            # print(area_execution_success)
            # print(area_execution_success["executionStatusUrl"])
            print("Creating area " + site_details["city"] + "...")

            create_status = "unkown"
            while create_status != "SUCCESS":
                area_create_status = apisvcs.validate_build_step(area_execution_success["executionStatusUrl"], HOSTNAME, dnacAuth["Token"])
                create_status_data = json.loads(area_create_status.text)
                # print(create_status_data)
                create_status = create_status_data["status"]
                print("Checking creation status of area " + site_details["city"] + "...")
                time.sleep(3)
                
            print("Area " + site_details["city"] + " successfully created")
            print("-------------------------------------------------------------")
            print(" ")



    for site_details in site_data["locations"]:

        newBuilding = apisvcs.site_build("building",
                                          site_details["city"], 
                                          site_details["bldg"],
                                          site_details["address"], 
                                          str(floor), 
                                          site_details["latitude"],
                                          site_details["longitude"],
                                          site_details["width"],
                                          site_details["length"],
                                          site_details["heigth"],
                                          HOSTNAME, 
                                          dnacAuth["Token"])

        building_execution_success = json.loads(newBuilding.text)
        # print(type(area_execution_success))
        # print(area_execution_success["executionStatusUrl"])

        print("Creating {} in area {}...".format(site_details["bldg"], site_details["city"]))

        create_status = "unkown"
        while create_status != "SUCCESS":
            building_create_status = apisvcs.validate_build_step(building_execution_success["executionStatusUrl"], HOSTNAME, dnacAuth["Token"])
            create_status_data = json.loads(building_create_status.text)
            # print(create_status_data)
            create_status = create_status_data["status"]
            print("Checking creation status of {} in area {}...".format(site_details["bldg"], site_details["city"]))
            time.sleep(3)

        print("{} successfully created in area {}".format(site_details["bldg"], site_details["city"]))
        print("-------------------------------------------------------------")
        print(" ")


    for site_details in site_data["locations"]:

        floor = site_details["floors"][0]
        totalFloors = len(site_details["floors"])

        i =  0

        while i <= totalFloors - 1:
            newFloor = apisvcs.site_build("floor",
                                          site_details["city"], 
                                          site_details["bldg"],
                                          site_details["address"], 
                                          str(site_details["floors"][i]), 
                                          site_details["latitude"],
                                          site_details["longitude"],
                                          site_details["width"],
                                          site_details["length"],
                                          site_details["heigth"],
                                          HOSTNAME, 
                                          dnacAuth["Token"])

            floor_execution_success = json.loads(newFloor.text)
            # print(type(area_execution_success))
            # print(area_execution_success["executionStatusUrl"])

            print("Creating Floor {} in {} {}...".format(site_details["floors"][i], site_details["city"], site_details["bldg"]))

            create_status = "unkown"
            while create_status != "SUCCESS":
                floor_create_status = apisvcs.validate_build_step(floor_execution_success["executionStatusUrl"], HOSTNAME, dnacAuth["Token"])
                create_status_data = json.loads(floor_create_status.text)
                # print(create_status_data)
                create_status = create_status_data["status"]
                print("Checking creation status of Floor {} in {} {}...".format(site_details["floors"][i], site_details["city"], site_details["bldg"]))
                time.sleep(3)

            print("Floor {} successfully created in {} {}".format(site_details["floors"][i], site_details["city"], site_details["bldg"]))
            print("-------------------------------------------------------------")
            print(" ")

            i = i + 1
