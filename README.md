### Building AI assitant using ollama

##### Ollama basics

- Models are stored in this format
    - manifests
    - blobs
    - metadata
- Newer version has different format for efficient storage 
    - manifest
    - manifest-v2
    - blobs
- Manifests, manifest-v2 is basically a sha index of what type of files are being stored by the model
- It gives you idea about which files has weights and which file focuses on parameters such as temperature or context window
- Files are stored in Content-Addressed Storage (CAS) for avoiding duplication and to prevent file corruption.
- CAS also helps with faster downloading if mutiple models use same param file or so on and is simpler for housekeeping files than complicated human readable naming conventions with versioning and so on.

##### Some basics

- We use openai api standards to call and talk to any models using ollama or groq etc.
- There three types of roles in the api call -- role : (user, assitant, system).
    - User is basically whoever is trying to ask questions or give command.
    - Assistant is models own replies.
    - System is the hidden instructions for the model for its own behavior.
- LLMs are STATELESS -- they dont remember previous text unless sent again using various techniques
    - Sliding window (lose context of older chat text)
    - Truncate (summarize the chat)
    - Compact (important point are sent instead of the whole chat)
    - RAG (a separat vertorized database for llm to access instead of sending the whole chat again and again)
