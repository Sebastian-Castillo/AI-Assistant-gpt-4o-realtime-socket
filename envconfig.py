#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
import os
from dotenv import load_dotenv
load_dotenv()

class DefaultConfig:
    """ Bot Configuration """

    az_openai_key="045bdcb95d814eb3a5c05592dfb44dad"
    az_open_ai_endpoint_name="inteligenciaartificial-pia-dev-oai-01"
    az_openai_api_version="2024-10-01-preview"
    model_name="gpt-4o-realtime-preview"
