"""
YAGNI - you are not going to need it

Always implement things when you actually need them, never when you just foresee
that you need them  - Ron Jeffries

Yagni is priniciple that encourages you to resist the temptaion to build features
or add flexibility until you are absolutely sure you need them.

Dont build for tomorrow. Build for today

Why premature work is harmful

1. wasted time and effort
2. increased complexity
3. Delayed value
4. Higher maintaince cost

When to Bend the rule.
dont do for speculative features(driven by what if) and known constraints (driven by 
real requirements, regulations, or contractual obligations)

Security and Compliance - audit logs encryptions
Architecture with known long-term constriants - sla for uptime, high availabilty 
systems
Reusable Libraries or framewors - librar that other teams depend on, some flexibility is 
excpected.
"""

# Real world Example
"""
Simple image upload resize that and save to local storage.
"""

# YAGNI Voilated

from abc import ABC, abstractmethod

# Interface for handling different media types
class IMediaHandler(ABC):
    @abstractmethod
    def can_handle(self, file_type: str) -> bool:
        pass

    @abstractmethod
    def process(self, file) -> object:
        pass

# Interface for storage providers
class IStorageProvider(ABC):
    @abstractmethod
    def store(self, file, path: str) -> None:
        pass

    @abstractmethod
    def retrieve(self, path: str) -> object:
        pass

    @abstractmethod
    def delete(self, path: str) -> None:
        pass

# Factory for creating media handlers
class MediaHandlerFactory:
    def __init__(self):
        self._handlers = {}

    def register(self, file_type: str, handler: IMediaHandler):
        self._handlers[file_type] = handler

    def get_handler(self, file_type: str) -> IMediaHandler:
        handler = self._handlers.get(file_type)
        if handler is None:
            raise ValueError(f"No handler for type: {file_type}")
        return handler

# Cloud storage adapter (not needed yet)
class CloudStorageAdapter(IStorageProvider):
    def __init__(self, bucket_name: str, region: str):
        self._bucket_name = bucket_name
        self._region = region

    def store(self, file, path: str) -> None:
        # Cloud upload logic - not implemented, not needed
        pass

    def retrieve(self, path: str) -> object:
        # Cloud download logic - not implemented, not needed
        return None

    def delete(self, path: str) -> None:
        # Cloud delete logic - not implemented, not needed
        pass

# Image handler (the only one actually needed)
class ImageMediaHandler(IMediaHandler):
    def can_handle(self, file_type: str) -> bool:
        return file_type == "image"

    def process(self, file) -> object:
        return self._resize(file, 300, 300)

    def _resize(self, file, width: int, height: int):
        # actual resize implementation
        return file

# The bloated engine that ties it all together
class MediaProcessingEngine:
    def __init__(self, handler_factory: MediaHandlerFactory,
                 storage_provider: IStorageProvider):
        self._handler_factory = handler_factory
        self._storage_provider = storage_provider

    def upload(self, file, file_type: str, path: str) -> None:
        handler = self._handler_factory.get_handler(file_type)
        processed = handler.process(file)
        self._storage_provider.store(processed, path)

# YAGNI Applied

class ImageUploader:
    def __init__(self, resizer, storage):
        self.resizer = resizer
        self.storage = storage

    def upload(self, image_file):
        resized = self.resizer.resize(image_file, 300, 300)
        self.storage.save(resized)