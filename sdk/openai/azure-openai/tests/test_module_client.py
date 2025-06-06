# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
import pytest
import pathlib
import openai
from devtools_testutils import AzureRecordedTestCase, get_credential
from conftest import (
    configure,
    ENV_AZURE_OPENAI_ENDPOINT,
    ENV_AZURE_OPENAI_KEY,
    LATEST,
    ENV_AZURE_OPENAI_NORTHCENTRALUS_ENDPOINT,
    ENV_AZURE_OPENAI_COMPLETIONS_NAME,
    ENV_AZURE_OPENAI_CHAT_COMPLETIONS_NAME,
    ENV_AZURE_OPENAI_EMBEDDINGS_NAME,
    ENV_AZURE_OPENAI_AUDIO_NAME,
    AZURE,
    reload,
    get_bearer_token_provider
)

audio_test_file = pathlib.Path(__file__).parent / "./assets/hello.m4a"


@pytest.mark.live_test_only
class TestModuleClient(AzureRecordedTestCase):

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_env_vars_key(self, client, api_type, api_version, **kwargs):
        with reload():
            os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            os.environ["OPENAI_API_VERSION"] = LATEST
            os.environ["AZURE_OPENAI_API_KEY"] = os.getenv(ENV_AZURE_OPENAI_KEY)
            os.environ["OPENAI_API_TYPE"] = "azure"

            try:
                completion = openai.completions.create(prompt="hello world", model=ENV_AZURE_OPENAI_COMPLETIONS_NAME)
                assert completion.id
                assert completion.object == "text_completion"
                assert completion.model
                assert completion.created
                assert completion.usage.completion_tokens is not None
                assert completion.usage.prompt_tokens is not None
                assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
                assert len(completion.choices) == 1
                assert completion.choices[0].finish_reason
                assert completion.choices[0].index is not None
                assert completion.choices[0].text is not None
            finally:
                del os.environ['AZURE_OPENAI_ENDPOINT']
                del os.environ['AZURE_OPENAI_API_KEY']
                del os.environ['OPENAI_API_VERSION']
                del os.environ["OPENAI_API_TYPE"]

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_env_vars_token(self, client, api_type, api_version, **kwargs):
        with reload():
            os.environ["AZURE_OPENAI_ENDPOINT"] = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            os.environ["OPENAI_API_VERSION"] = LATEST
            os.environ["AZURE_OPENAI_AD_TOKEN"] = get_credential().get_token("https://cognitiveservices.azure.com/.default").token
            os.environ["OPENAI_API_TYPE"] = "azure"

            try:
                completion = openai.completions.create(prompt="hello world", model=ENV_AZURE_OPENAI_COMPLETIONS_NAME)
                assert completion.id
                assert completion.object == "text_completion"
                assert completion.model
                assert completion.created
                assert completion.usage.completion_tokens is not None
                assert completion.usage.prompt_tokens is not None
                assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
                assert len(completion.choices) == 1
                assert completion.choices[0].finish_reason
                assert completion.choices[0].index is not None
                assert completion.choices[0].text is not None
            finally:
                del os.environ['AZURE_OPENAI_ENDPOINT']
                del os.environ['AZURE_OPENAI_AD_TOKEN']
                del os.environ['OPENAI_API_VERSION']
                del os.environ["OPENAI_API_TYPE"]

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_api_key(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.api_key = os.getenv(ENV_AZURE_OPENAI_KEY)
            openai.api_version = LATEST

            completion = openai.completions.create(prompt="hello world", model=ENV_AZURE_OPENAI_COMPLETIONS_NAME)
            assert completion.id
            assert completion.object == "text_completion"
            assert completion.model
            assert completion.created
            assert completion.usage.completion_tokens is not None
            assert completion.usage.prompt_tokens is not None
            assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
            assert len(completion.choices) == 1
            assert completion.choices[0].finish_reason
            assert completion.choices[0].index is not None
            assert completion.choices[0].text is not None


    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_ad_token(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.azure_ad_token = get_credential().get_token("https://cognitiveservices.azure.com/.default").token
            openai.api_version = LATEST

            completion = openai.completions.create(prompt="hello world", model=ENV_AZURE_OPENAI_COMPLETIONS_NAME)
            assert completion.id
            assert completion.object == "text_completion"
            assert completion.model
            assert completion.created
            assert completion.usage.completion_tokens is not None
            assert completion.usage.prompt_tokens is not None
            assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
            assert len(completion.choices) == 1
            assert completion.choices[0].finish_reason
            assert completion.choices[0].index is not None
            assert completion.choices[0].text is not None


    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_completions(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.azure_ad_token_provider = get_bearer_token_provider(get_credential(), "https://cognitiveservices.azure.com/.default")
            openai.api_version = LATEST

            completion = openai.completions.create(prompt="hello world", model=ENV_AZURE_OPENAI_COMPLETIONS_NAME)
            assert completion.id
            assert completion.object == "text_completion"
            assert completion.model
            assert completion.created
            assert completion.usage.completion_tokens is not None
            assert completion.usage.prompt_tokens is not None
            assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
            assert len(completion.choices) == 1
            assert completion.choices[0].finish_reason
            assert completion.choices[0].index is not None
            assert completion.choices[0].text is not None

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_chat_completions(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.azure_ad_token_provider = get_bearer_token_provider(get_credential(), "https://cognitiveservices.azure.com/.default")
            openai.api_version = LATEST

            messages = [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Who won the world series in 2020?"}
            ]

            completion = openai.chat.completions.create(messages=messages, model=ENV_AZURE_OPENAI_CHAT_COMPLETIONS_NAME)
            assert completion.id
            assert completion.object == "chat.completion"
            assert completion.model
            assert completion.created
            assert completion.usage.completion_tokens is not None
            assert completion.usage.prompt_tokens is not None
            assert completion.usage.total_tokens == completion.usage.completion_tokens + completion.usage.prompt_tokens
            assert len(completion.choices) == 1
            assert completion.choices[0].finish_reason
            assert completion.choices[0].index is not None
            assert completion.choices[0].message.content is not None
            assert completion.choices[0].message.role

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_embeddings(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.azure_ad_token_provider = get_bearer_token_provider(get_credential(), "https://cognitiveservices.azure.com/.default")
            openai.api_version = LATEST

            embedding = openai.embeddings.create(input="hello world", model=ENV_AZURE_OPENAI_EMBEDDINGS_NAME)
            assert embedding.object == "list"
            assert embedding.model
            assert embedding.usage.prompt_tokens is not None
            assert embedding.usage.total_tokens is not None
            assert len(embedding.data) == 1
            assert embedding.data[0].object == "embedding"
            assert embedding.data[0].index is not None
            assert len(embedding.data[0].embedding) > 0

    @pytest.mark.skip("InternalServerError, opened issue")
    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_models(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_ENDPOINT)
            openai.azure_ad_token_provider = get_bearer_token_provider(get_credential(), "https://cognitiveservices.azure.com/.default")
            openai.api_version = LATEST

            models = openai.models.list()
            for model in models:
                assert model.id

            model = openai.models.retrieve(model=ENV_AZURE_OPENAI_CHAT_COMPLETIONS_NAME)
            assert model.id

    @configure
    @pytest.mark.parametrize("api_type, api_version", [(AZURE, LATEST)])
    def test_module_client_audio(self, client, api_type, api_version, **kwargs):
        with reload():
            openai.api_type= "azure"
            openai.azure_endpoint = os.getenv(ENV_AZURE_OPENAI_NORTHCENTRALUS_ENDPOINT)
            openai.azure_ad_token_provider = get_bearer_token_provider(get_credential(), "https://cognitiveservices.azure.com/.default")
            openai.api_version = LATEST

            result = openai.audio.transcriptions.create(
                file=open(audio_test_file, "rb"),
                model=ENV_AZURE_OPENAI_AUDIO_NAME
            )
            assert result.text == "Hello."

            result = openai.audio.translations.create(
                file=open(audio_test_file, "rb"),
                model=ENV_AZURE_OPENAI_AUDIO_NAME
            )
            assert result.text == "Hello."
