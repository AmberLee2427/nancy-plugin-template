"""A Nexus-Nancy plugin template."""

from typing import Any, Dict, List, Optional
from nexus_nancy.tools import ToolDefinition
from nexus_nancy.provider import LLMProvider


def hello(name: str = "World") -> str:
    """A simple hello world plugin for testing."""
    return f"Hello from plugin, {name}!"


def register_tools():
    """Register plugin tools. Called by Nancy at startup."""
    return [
        ToolDefinition(
            name="plugin_hello",
            description="A hello world plugin. Use to verify your plugin loads correctly.",
            parameters={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Name to greet",
                        "default": "World"
                    }
                },
                "required": []
            },
            handler=hello,
            # slash_command: Optional command users can type directly (e.g., "/hello")
            slash_command=None
        )
    ]


class ExampleCustomProvider(LLMProvider):
    """
    Example of a custom LLM provider.
    
    To use this, set 'provider: example' in your nnancy.yaml.
    """
    def __init__(self, cfg, workspace_root):
        self.cfg = cfg
        self.workspace_root = workspace_root

    def chat(
        self,
        messages: List[Dict[str, Any]],
        tools: Optional[List[Dict[str, Any]]] = None,
        *,
        tool_choice: Optional[Any] = None,
        parallel_tool_calls: Optional[bool] = None,
        response_format: Optional[Dict[str, Any]] = None,
        extra_body: Optional[Dict[str, Any]] = None,
        require_bash_tool: bool = True,
    ) -> Dict[str, Any]:
        """
        Repackage standard OpenAI-style requests for your specific backend.
        """
        # Example: Mock response
        return {
            "choices": [
                {
                    "message": {
                        "role": "assistant",
                        "content": "[RESPONSE]This is a response from the custom provider.[/RESPONSE][EOT]"
                    },
                    "finish_reason": "stop"
                }
            ]
        }

    def probe_capabilities(self) -> Dict[str, bool]:
        """Return supported features."""
        return {
            "native_tools": False,
            "reasoning_channel": False
        }


def register_providers():
    """Register custom LLM providers."""
    return {
        "example": ExampleCustomProvider
    }
