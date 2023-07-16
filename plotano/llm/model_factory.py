"""LLM factory"""
from typing import Union

from plotano.llm.constants import LlmName
from plotano.llm.abs_llm import AbsLlm
from plotano.llm.openai import OpenAIModel


class ModelFactory:
    """LLM factory"""
    @staticmethod
    def create_model(model_name: Union[str, LlmName]) -> AbsLlm:
        """
        Create a language model based on the given name.

        Args:
            model_name (Union[str, LlmName]): The name of the language model.

        Returns:
            AbsLlm: An instance of the language model.

        Raises:
            ValueError: If the given model name is not valid.
        """
        try:
            model_name = LlmName(model_name)
            if model_name == LlmName.OPENAI:
                return OpenAIModel()
            else:
                raise ValueError(f"[llm_factory]: Unknown model: "
                                 f"{model_name}")
            # elif model_name == LlmName.LLAMA_CPP:
            #     return LlamaCppModel()
            # elif model_name == LlmName.SAGEMAKER:
            #     return SageMaker()
        except ValueError as ex:
            raise ValueError(f"[llm_factory]: Unknown model: "
                             f"{model_name}") from ex