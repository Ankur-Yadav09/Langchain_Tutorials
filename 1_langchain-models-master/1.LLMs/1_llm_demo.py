# Initialize a model
## The easiest way to get started with a standalone model in LangChain
## is to use init_chat_model to initialize one from a chat model provider of your choice.

from langchain.chat_models import init_chat_model 
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from numpy import number
from openai import api_key, timeout
load_dotenv()

# Method 1: Initialize a model using init_chat_model
model = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="groq"
    )

# init_chat_model
## Initialize a chat model from any supported provider using a unified interface.

# Two main use cases:

## Fixed model – specify the model upfront and get a ready-to-use chat model.
## Configurable model – choose to specify parameters (including model name) at runtime via config. 
## Makes it easy to switch between models/providers without changing your code

# Parameters
## A chat model takes parameters that can be used to configure its behavior.
## The full set of supported parameters varies by model and provider, but standard ones include:

# 1) model *stringrequired*
## The name or identifier of the specific model you want to use with a provider. 
## You can also specify both the model and its provider in a single argument using the ’:’ format, for example, ‘openai:o1’.

# 2) api_key *string*
## The key required for authenticating with the model’s provider. 
## This is usually issued when you sign up for access to the model.
##  Often accessed by setting an environment variable.

# 3) temperature *number*
## Controls the randomness of the model’s output. A higher number makes responses more creative; lower ones make them more deterministic.

# 4) max_tokens *number*
## Limits the total number of tokens in the response, effectively controlling how long the output can be.

# 5) timeout *number*
## The maximum time (in seconds) to wait for a response from the model before canceling the request.

# 6) max_retries *number*default:"6"
## The maximum number of attempts the system will make to resend a request if it fails 
## due to issues like network timeouts or rate limits. Retries use exponential backoff with jitter.
##  Network errors, rate limits (429), and server errors (5xx) are retried automatically. 
## Client errors such as 401 (unauthorized) or 404 are not retried. 
## For long-running agent tasks on unreliable networks, consider increasing this to 10–15.

# Using init_chat_model, pass these parameters as inline **kwargs:
# Initialize using model parameters
# model = init_chat_model(
#     "claude-sonnet-4-6",
#     # Kwargs passed to the model:
#     temperature=0.7,
#     timeout=30,
#     max_tokens=1000,
#     max_retries=6,  # Default; increase for unreliable networks
# )

# Invocation
## A chat model must be invoked to generate an output. There are three primary invocation methods,
##  each suited to different use cases.

# 1) Invoke
## The most straightforward way to call a model is to use invoke() 
# with a single message or a list of messages.

result = model.invoke("What is the capital of India?")
print("Method 1 (Using Invoke):", result.content)
print("//-----------------------------//")

# 2) Stream
## Most models can stream their output content while it is being generated. 
## By displaying output progressively, streaming significantly improves 
## user experience, particularly for longer responses.

## Calling stream() returns an iterator that yields output chunks as they are produced. 
## You can use a loop to process each chunk in real-time:
print("Method 2 (Using Stream):")
for chunk in model.stream("What is the capital of India?"):
    print(chunk.text, end="|", flush=True)
print("//-----------------------------//")
# Batch
## Batching a collection of independent requests to a model can significantly improve performance 
## and reduce costs, as the processing can be done in parallel:

responses = model.batch([
    "What is the capital of Japan?",
    "What is the capital of India?"
])
print("Method 3 (Using Batch):")
for response in responses:
    print(response.content)
print("//-----------------------------//")

# Method 2: Initialize a model using the provider's class directly
llm = ChatGroq(
    model="llama-3.3-70b-versatile"
)

result = llm.invoke("What is the capital of Japan?")

print("Method 2 (Using Direct Class):", result.content)
print("//-----------------------------//")
