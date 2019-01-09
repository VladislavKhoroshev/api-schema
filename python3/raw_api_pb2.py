# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raw_api.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='raw_api.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=_b('\342?\026\n\024im.dlg.grpc.services'),
  serialized_pb=_b('\n\rraw_api.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x15scalapb/scalapb.proto\"\xa8\x01\n\x11RequestRawRequest\x12<\n\x07service\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible\x12\x37\n\x04\x62ody\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.BytesValueB\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"^\n\x12ResponseRawRequest\x12)\n\x04\x62ody\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.BytesValue:\x1d\xe2?\x1a\n\x18im.dlg.grpc.GrpcResponse2t\n\x06RawAPI\x12j\n\nRawRequest\x12\x19.dialog.RequestRawRequest\x1a\x1a.dialog.ResponseRawRequest\"%\x82\xd3\xe4\x93\x02\x1f\"\x1a/v1/grpc/RawAPI/RawRequest:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])




_REQUESTRAWREQUEST = _descriptor.Descriptor(
  name='RequestRawRequest',
  full_name='dialog.RequestRawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='service', full_name='dialog.RequestRawRequest.service', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='body', full_name='dialog.RequestRawRequest.body', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\010\n\006hidden'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\031\n\027im.dlg.grpc.GrpcRequest'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=130,
  serialized_end=298,
)


_RESPONSERAWREQUEST = _descriptor.Descriptor(
  name='ResponseRawRequest',
  full_name='dialog.ResponseRawRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='body', full_name='dialog.ResponseRawRequest.body', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\342?\032\n\030im.dlg.grpc.GrpcResponse'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=300,
  serialized_end=394,
)

_REQUESTRAWREQUEST.fields_by_name['service'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_REQUESTRAWREQUEST.fields_by_name['body'].message_type = google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE
_RESPONSERAWREQUEST.fields_by_name['body'].message_type = google_dot_protobuf_dot_wrappers__pb2._BYTESVALUE
DESCRIPTOR.message_types_by_name['RequestRawRequest'] = _REQUESTRAWREQUEST
DESCRIPTOR.message_types_by_name['ResponseRawRequest'] = _RESPONSERAWREQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestRawRequest = _reflection.GeneratedProtocolMessageType('RequestRawRequest', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTRAWREQUEST,
  __module__ = 'raw_api_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRawRequest)
  ))
_sym_db.RegisterMessage(RequestRawRequest)

ResponseRawRequest = _reflection.GeneratedProtocolMessageType('ResponseRawRequest', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSERAWREQUEST,
  __module__ = 'raw_api_pb2'
  # @@protoc_insertion_point(class_scope:dialog.ResponseRawRequest)
  ))
_sym_db.RegisterMessage(ResponseRawRequest)


DESCRIPTOR._options = None
_REQUESTRAWREQUEST.fields_by_name['service']._options = None
_REQUESTRAWREQUEST.fields_by_name['body']._options = None
_REQUESTRAWREQUEST._options = None
_RESPONSERAWREQUEST._options = None

_RAWAPI = _descriptor.ServiceDescriptor(
  name='RawAPI',
  full_name='dialog.RawAPI',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=396,
  serialized_end=512,
  methods=[
  _descriptor.MethodDescriptor(
    name='RawRequest',
    full_name='dialog.RawAPI.RawRequest',
    index=0,
    containing_service=None,
    input_type=_REQUESTRAWREQUEST,
    output_type=_RESPONSERAWREQUEST,
    serialized_options=_b('\202\323\344\223\002\037\"\032/v1/grpc/RawAPI/RawRequest:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_RAWAPI)

DESCRIPTOR.services_by_name['RawAPI'] = _RAWAPI

# @@protoc_insertion_point(module_scope)
