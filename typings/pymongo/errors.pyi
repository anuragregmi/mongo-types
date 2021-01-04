from typing import Any, Dict, Iterable, List, Optional

from bson.errors import InvalidDocument
from typing_extensions import TypedDict

class PyMongoError(Exception):
    def __init__(
        self, message: str = ..., error_labels: Optional[Iterable[str]] = ...
    ) -> None: ...
    def has_error_label(self, label: str) -> bool: ...

class ProtocolError(PyMongoError): ...
class ConnectionFailure(PyMongoError): ...

class AutoReconnect(ConnectionFailure):
    def __init__(
        self, message: str = ..., error_labels: Optional[Iterable[str]] = ...
    ) -> None: ...

class NetworkTimeout(AutoReconnect): ...

class NotMasterError(AutoReconnect):
    def __init__(
        self, message: str = ..., error_labels: Optional[Iterable[str]] = ...
    ) -> None: ...

class ServerSelectionTimeoutError(AutoReconnect): ...
class ConfigurationError(PyMongoError): ...

class _WriteError(TypedDict, total=False):
    index: int
    code: int
    errmsg: str
    op: Dict[str, Any]

class _OpFailureDetails(TypedDict):
    nInserted: int
    nUpserted: int
    nMatched: int
    nModified: int
    nRemoved: int
    upserted: List[Any]
    writeErrors: List[_WriteError]
    writeConcernErrors: List[Any]

class OperationFailure(PyMongoError):
    def __init__(
        self,
        error: Any,
        code: int = ...,
        details: Optional[Any] = ...,
        max_wire_version: Optional[Any] = ...,
    ) -> None: ...
    @property
    def code(self) -> int: ...
    @property
    def details(self) -> _OpFailureDetails: ...

class CursorNotFound(OperationFailure): ...
class ExecutionTimeout(OperationFailure): ...
class WriteConcernError(OperationFailure): ...
class WriteError(OperationFailure): ...
class WTimeoutError(WriteConcernError): ...
class DuplicateKeyError(WriteError): ...

class BulkWriteError(OperationFailure):
    def __init__(self, results: Any) -> None: ...

class InvalidOperation(PyMongoError): ...
class InvalidName(PyMongoError): ...
class CollectionInvalid(PyMongoError): ...
class InvalidURI(ConfigurationError): ...
class ExceededMaxWaiters(PyMongoError): ...
class DocumentTooLarge(InvalidDocument): ...

class EncryptionError(PyMongoError):
    def __init__(self, cause: Any) -> None: ...
    @property
    def cause(self) -> Any: ...

class _OperationCancelled(AutoReconnect): ...
