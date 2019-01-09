# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: typing_and_online.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from . import definitions_pb2 as definitions__pb2
from . import miscellaneous_pb2 as miscellaneous__pb2
from . import peers_pb2 as peers__pb2
from .scalapb import scalapb_pb2 as scalapb_dot_scalapb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='typing_and_online.proto',
  package='dialog',
  syntax='proto3',
  serialized_options=_b('\342?\026\n\024im.dlg.grpc.services'),
  serialized_pb=_b('\n\x17typing_and_online.proto\x12\x06\x64ialog\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x11\x64\x65\x66initions.proto\x1a\x13miscellaneous.proto\x1a\x0bpeers.proto\x1a\x15scalapb/scalapb.proto\"\x93\x01\n\rRequestTyping\x12,\n\x04peer\x18\x01 \x01(\x0b\x32\x0f.dialog.OutPeerB\r\x8a\xea\x30\t\n\x07visible\x12\x36\n\x0btyping_type\x18\x03 \x01(\x0e\x32\x12.dialog.TypingTypeB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\x97\x01\n\x11RequestStopTyping\x12,\n\x04peer\x18\x01 \x01(\x0b\x32\x0f.dialog.OutPeerB\r\x8a\xea\x30\t\n\x07visible\x12\x36\n\x0btyping_type\x18\x02 \x01(\x0e\x32\x12.dialog.TypingTypeB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\xf0\x01\n\x10RequestSetOnline\x12 \n\tis_online\x18\x01 \x01(\x08\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1e\n\x07timeout\x18\x02 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\x12\x36\n\x0b\x64\x65vice_type\x18\x03 \x01(\x0e\x32\x12.dialog.DeviceTypeB\r\x8a\xea\x30\t\n\x07visible\x12\x44\n\x0f\x64\x65vice_category\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValueB\r\x8a\xea\x30\t\n\x07visible:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\":\n\x18UpdatePauseNotifications\x12\x1e\n\x07timeout\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\"\x1c\n\x1aUpdateRestoreNotifications\"X\n\x19RequestPauseNotifications\x12\x1d\n\x07timeout\x18\x01 \x01(\x05\x42\x0c\x8a\xea\x30\x08\n\x06hidden:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\";\n\x1bRequestRestoreNotifications:\x1c\xe2?\x19\n\x17im.dlg.grpc.GrpcRequest\"\x8d\x01\n\x0cUpdateTyping\x12)\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.PeerB\r\x8a\xea\x30\t\n\x07visible\x12\x1a\n\x03uid\x18\x02 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x36\n\x0btyping_type\x18\x03 \x01(\x0e\x32\x12.dialog.TypingTypeB\r\x8a\xea\x30\t\n\x07visible\"\x90\x01\n\x10UpdateTypingStop\x12)\n\x04peer\x18\x01 \x01(\x0b\x32\x0c.dialog.PeerB\r\x8a\xea\x30\t\n\x07visible\x12\x1a\n\x03uid\x18\x02 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x35\n\x0btyping_type\x18\x03 \x01(\x0e\x32\x12.dialog.TypingTypeB\x0c\x8a\xea\x30\x08\n\x06hidden\"\x8e\x01\n\x10UpdateUserOnline\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\'\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0e\x32\x12.dialog.DeviceType\x12\x35\n\x0f\x64\x65vice_category\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8f\x01\n\x11UpdateUserOffline\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\'\n\x0b\x64\x65vice_type\x18\x02 \x01(\x0e\x32\x12.dialog.DeviceType\x12\x35\n\x0f\x64\x65vice_category\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xad\x01\n\x12UpdateUserLastSeen\x12\x1a\n\x03uid\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1b\n\x04\x64\x61te\x18\x02 \x01(\x03\x42\r\x8a\xea\x30\t\n\x07visible\x12\'\n\x0b\x64\x65vice_type\x18\x03 \x01(\x0e\x32\x12.dialog.DeviceType\x12\x35\n\x0f\x64\x65vice_category\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"R\n\x11UpdateGroupOnline\x12\x1f\n\x08group_id\x18\x01 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible\x12\x1c\n\x05\x63ount\x18\x02 \x01(\x05\x42\r\x8a\xea\x30\t\n\x07visible*9\n\nTypingType\x12\x16\n\x12TYPINGTYPE_UNKNOWN\x10\x00\x12\x13\n\x0fTYPINGTYPE_TEXT\x10\x01*\xd4\x01\n\nDeviceType\x12\x16\n\x12\x44\x45VICETYPE_UNKNOWN\x10\x00\x12\x16\n\x12\x44\x45VICETYPE_GENERIC\x10\x01\x12\x11\n\rDEVICETYPE_PC\x10\x02\x12\x15\n\x11\x44\x45VICETYPE_MOBILE\x10\x03\x12\x15\n\x11\x44\x45VICETYPE_TABLET\x10\x04\x12\x14\n\x10\x44\x45VICETYPE_WATCH\x10\x05\x12\x15\n\x11\x44\x45VICETYPE_MIRROR\x10\x06\x12\x12\n\x0e\x44\x45VICETYPE_CAR\x10\x07\x12\x14\n\x10\x44\x45VICETYPE_TABLE\x10\x08\x32\xe5\x04\n\x0fTypingAndOnline\x12\x61\n\x06Typing\x12\x15.dialog.RequestTyping\x1a\x14.dialog.ResponseVoid\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/grpc/TypingAndOnline/Typing:\x01*\x12m\n\nStopTyping\x12\x19.dialog.RequestStopTyping\x1a\x14.dialog.ResponseVoid\".\x82\xd3\xe4\x93\x02(\"#/v1/grpc/TypingAndOnline/StopTyping:\x01*\x12j\n\tSetOnline\x12\x18.dialog.RequestSetOnline\x1a\x14.dialog.ResponseVoid\"-\x82\xd3\xe4\x93\x02\'\"\"/v1/grpc/TypingAndOnline/SetOnline:\x01*\x12\x85\x01\n\x12PauseNotifications\x12!.dialog.RequestPauseNotifications\x1a\x14.dialog.ResponseVoid\"6\x82\xd3\xe4\x93\x02\x30\"+/v1/grpc/TypingAndOnline/PauseNotifications:\x01*\x12\x8b\x01\n\x14RestoreNotifications\x12#.dialog.RequestRestoreNotifications\x1a\x14.dialog.ResponseVoid\"8\x82\xd3\xe4\x93\x02\x32\"-/v1/grpc/TypingAndOnline/RestoreNotifications:\x01*B\x19\xe2?\x16\n\x14im.dlg.grpc.servicesb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,google_dot_api_dot_annotations__pb2.DESCRIPTOR,definitions__pb2.DESCRIPTOR,miscellaneous__pb2.DESCRIPTOR,peers__pb2.DESCRIPTOR,scalapb_dot_scalapb__pb2.DESCRIPTOR,])

_TYPINGTYPE = _descriptor.EnumDescriptor(
  name='TypingType',
  full_name='dialog.TypingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='TYPINGTYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TYPINGTYPE_TEXT', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1803,
  serialized_end=1860,
)
_sym_db.RegisterEnumDescriptor(_TYPINGTYPE)

TypingType = enum_type_wrapper.EnumTypeWrapper(_TYPINGTYPE)
_DEVICETYPE = _descriptor.EnumDescriptor(
  name='DeviceType',
  full_name='dialog.DeviceType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_GENERIC', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_PC', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_MOBILE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_TABLET', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_WATCH', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_MIRROR', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_CAR', index=7, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DEVICETYPE_TABLE', index=8, number=8,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1863,
  serialized_end=2075,
)
_sym_db.RegisterEnumDescriptor(_DEVICETYPE)

DeviceType = enum_type_wrapper.EnumTypeWrapper(_DEVICETYPE)
TYPINGTYPE_UNKNOWN = 0
TYPINGTYPE_TEXT = 1
DEVICETYPE_UNKNOWN = 0
DEVICETYPE_GENERIC = 1
DEVICETYPE_PC = 2
DEVICETYPE_MOBILE = 3
DEVICETYPE_TABLET = 4
DEVICETYPE_WATCH = 5
DEVICETYPE_MIRROR = 6
DEVICETYPE_CAR = 7
DEVICETYPE_TABLE = 8



_REQUESTTYPING = _descriptor.Descriptor(
  name='RequestTyping',
  full_name='dialog.RequestTyping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.RequestTyping.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typing_type', full_name='dialog.RequestTyping.typing_type', index=1,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
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
  serialized_start=174,
  serialized_end=321,
)


_REQUESTSTOPTYPING = _descriptor.Descriptor(
  name='RequestStopTyping',
  full_name='dialog.RequestStopTyping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.RequestStopTyping.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typing_type', full_name='dialog.RequestStopTyping.typing_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
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
  serialized_start=324,
  serialized_end=475,
)


_REQUESTSETONLINE = _descriptor.Descriptor(
  name='RequestSetOnline',
  full_name='dialog.RequestSetOnline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_online', full_name='dialog.RequestSetOnline.is_online', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timeout', full_name='dialog.RequestSetOnline.timeout', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='dialog.RequestSetOnline.device_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_category', full_name='dialog.RequestSetOnline.device_category', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
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
  serialized_start=478,
  serialized_end=718,
)


_UPDATEPAUSENOTIFICATIONS = _descriptor.Descriptor(
  name='UpdatePauseNotifications',
  full_name='dialog.UpdatePauseNotifications',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='dialog.UpdatePauseNotifications.timeout', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=720,
  serialized_end=778,
)


_UPDATERESTORENOTIFICATIONS = _descriptor.Descriptor(
  name='UpdateRestoreNotifications',
  full_name='dialog.UpdateRestoreNotifications',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=780,
  serialized_end=808,
)


_REQUESTPAUSENOTIFICATIONS = _descriptor.Descriptor(
  name='RequestPauseNotifications',
  full_name='dialog.RequestPauseNotifications',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timeout', full_name='dialog.RequestPauseNotifications.timeout', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=810,
  serialized_end=898,
)


_REQUESTRESTORENOTIFICATIONS = _descriptor.Descriptor(
  name='RequestRestoreNotifications',
  full_name='dialog.RequestRestoreNotifications',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=900,
  serialized_end=959,
)


_UPDATETYPING = _descriptor.Descriptor(
  name='UpdateTyping',
  full_name='dialog.UpdateTyping',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.UpdateTyping.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateTyping.uid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typing_type', full_name='dialog.UpdateTyping.typing_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=962,
  serialized_end=1103,
)


_UPDATETYPINGSTOP = _descriptor.Descriptor(
  name='UpdateTypingStop',
  full_name='dialog.UpdateTypingStop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peer', full_name='dialog.UpdateTypingStop.peer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateTypingStop.uid', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='typing_type', full_name='dialog.UpdateTypingStop.typing_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\010\n\006hidden'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1106,
  serialized_end=1250,
)


_UPDATEUSERONLINE = _descriptor.Descriptor(
  name='UpdateUserOnline',
  full_name='dialog.UpdateUserOnline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateUserOnline.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='dialog.UpdateUserOnline.device_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_category', full_name='dialog.UpdateUserOnline.device_category', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1253,
  serialized_end=1395,
)


_UPDATEUSEROFFLINE = _descriptor.Descriptor(
  name='UpdateUserOffline',
  full_name='dialog.UpdateUserOffline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateUserOffline.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='dialog.UpdateUserOffline.device_type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_category', full_name='dialog.UpdateUserOffline.device_category', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1398,
  serialized_end=1541,
)


_UPDATEUSERLASTSEEN = _descriptor.Descriptor(
  name='UpdateUserLastSeen',
  full_name='dialog.UpdateUserLastSeen',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uid', full_name='dialog.UpdateUserLastSeen.uid', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date', full_name='dialog.UpdateUserLastSeen.date', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_type', full_name='dialog.UpdateUserLastSeen.device_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='device_category', full_name='dialog.UpdateUserLastSeen.device_category', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1544,
  serialized_end=1717,
)


_UPDATEGROUPONLINE = _descriptor.Descriptor(
  name='UpdateGroupOnline',
  full_name='dialog.UpdateGroupOnline',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='dialog.UpdateGroupOnline.group_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='count', full_name='dialog.UpdateGroupOnline.count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\3520\t\n\007visible'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1719,
  serialized_end=1801,
)

_REQUESTTYPING.fields_by_name['peer'].message_type = peers__pb2._OUTPEER
_REQUESTTYPING.fields_by_name['typing_type'].enum_type = _TYPINGTYPE
_REQUESTSTOPTYPING.fields_by_name['peer'].message_type = peers__pb2._OUTPEER
_REQUESTSTOPTYPING.fields_by_name['typing_type'].enum_type = _TYPINGTYPE
_REQUESTSETONLINE.fields_by_name['device_type'].enum_type = _DEVICETYPE
_REQUESTSETONLINE.fields_by_name['device_category'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATETYPING.fields_by_name['peer'].message_type = peers__pb2._PEER
_UPDATETYPING.fields_by_name['typing_type'].enum_type = _TYPINGTYPE
_UPDATETYPINGSTOP.fields_by_name['peer'].message_type = peers__pb2._PEER
_UPDATETYPINGSTOP.fields_by_name['typing_type'].enum_type = _TYPINGTYPE
_UPDATEUSERONLINE.fields_by_name['device_type'].enum_type = _DEVICETYPE
_UPDATEUSERONLINE.fields_by_name['device_category'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEUSEROFFLINE.fields_by_name['device_type'].enum_type = _DEVICETYPE
_UPDATEUSEROFFLINE.fields_by_name['device_category'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_UPDATEUSERLASTSEEN.fields_by_name['device_type'].enum_type = _DEVICETYPE
_UPDATEUSERLASTSEEN.fields_by_name['device_category'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['RequestTyping'] = _REQUESTTYPING
DESCRIPTOR.message_types_by_name['RequestStopTyping'] = _REQUESTSTOPTYPING
DESCRIPTOR.message_types_by_name['RequestSetOnline'] = _REQUESTSETONLINE
DESCRIPTOR.message_types_by_name['UpdatePauseNotifications'] = _UPDATEPAUSENOTIFICATIONS
DESCRIPTOR.message_types_by_name['UpdateRestoreNotifications'] = _UPDATERESTORENOTIFICATIONS
DESCRIPTOR.message_types_by_name['RequestPauseNotifications'] = _REQUESTPAUSENOTIFICATIONS
DESCRIPTOR.message_types_by_name['RequestRestoreNotifications'] = _REQUESTRESTORENOTIFICATIONS
DESCRIPTOR.message_types_by_name['UpdateTyping'] = _UPDATETYPING
DESCRIPTOR.message_types_by_name['UpdateTypingStop'] = _UPDATETYPINGSTOP
DESCRIPTOR.message_types_by_name['UpdateUserOnline'] = _UPDATEUSERONLINE
DESCRIPTOR.message_types_by_name['UpdateUserOffline'] = _UPDATEUSEROFFLINE
DESCRIPTOR.message_types_by_name['UpdateUserLastSeen'] = _UPDATEUSERLASTSEEN
DESCRIPTOR.message_types_by_name['UpdateGroupOnline'] = _UPDATEGROUPONLINE
DESCRIPTOR.enum_types_by_name['TypingType'] = _TYPINGTYPE
DESCRIPTOR.enum_types_by_name['DeviceType'] = _DEVICETYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RequestTyping = _reflection.GeneratedProtocolMessageType('RequestTyping', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTTYPING,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestTyping)
  ))
_sym_db.RegisterMessage(RequestTyping)

RequestStopTyping = _reflection.GeneratedProtocolMessageType('RequestStopTyping', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSTOPTYPING,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestStopTyping)
  ))
_sym_db.RegisterMessage(RequestStopTyping)

RequestSetOnline = _reflection.GeneratedProtocolMessageType('RequestSetOnline', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTSETONLINE,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestSetOnline)
  ))
_sym_db.RegisterMessage(RequestSetOnline)

UpdatePauseNotifications = _reflection.GeneratedProtocolMessageType('UpdatePauseNotifications', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEPAUSENOTIFICATIONS,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdatePauseNotifications)
  ))
_sym_db.RegisterMessage(UpdatePauseNotifications)

UpdateRestoreNotifications = _reflection.GeneratedProtocolMessageType('UpdateRestoreNotifications', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESTORENOTIFICATIONS,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateRestoreNotifications)
  ))
_sym_db.RegisterMessage(UpdateRestoreNotifications)

RequestPauseNotifications = _reflection.GeneratedProtocolMessageType('RequestPauseNotifications', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTPAUSENOTIFICATIONS,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestPauseNotifications)
  ))
_sym_db.RegisterMessage(RequestPauseNotifications)

RequestRestoreNotifications = _reflection.GeneratedProtocolMessageType('RequestRestoreNotifications', (_message.Message,), dict(
  DESCRIPTOR = _REQUESTRESTORENOTIFICATIONS,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.RequestRestoreNotifications)
  ))
_sym_db.RegisterMessage(RequestRestoreNotifications)

UpdateTyping = _reflection.GeneratedProtocolMessageType('UpdateTyping', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETYPING,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateTyping)
  ))
_sym_db.RegisterMessage(UpdateTyping)

UpdateTypingStop = _reflection.GeneratedProtocolMessageType('UpdateTypingStop', (_message.Message,), dict(
  DESCRIPTOR = _UPDATETYPINGSTOP,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateTypingStop)
  ))
_sym_db.RegisterMessage(UpdateTypingStop)

UpdateUserOnline = _reflection.GeneratedProtocolMessageType('UpdateUserOnline', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERONLINE,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateUserOnline)
  ))
_sym_db.RegisterMessage(UpdateUserOnline)

UpdateUserOffline = _reflection.GeneratedProtocolMessageType('UpdateUserOffline', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSEROFFLINE,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateUserOffline)
  ))
_sym_db.RegisterMessage(UpdateUserOffline)

UpdateUserLastSeen = _reflection.GeneratedProtocolMessageType('UpdateUserLastSeen', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEUSERLASTSEEN,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateUserLastSeen)
  ))
_sym_db.RegisterMessage(UpdateUserLastSeen)

UpdateGroupOnline = _reflection.GeneratedProtocolMessageType('UpdateGroupOnline', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEGROUPONLINE,
  __module__ = 'typing_and_online_pb2'
  # @@protoc_insertion_point(class_scope:dialog.UpdateGroupOnline)
  ))
_sym_db.RegisterMessage(UpdateGroupOnline)


DESCRIPTOR._options = None
_REQUESTTYPING.fields_by_name['peer']._options = None
_REQUESTTYPING.fields_by_name['typing_type']._options = None
_REQUESTTYPING._options = None
_REQUESTSTOPTYPING.fields_by_name['peer']._options = None
_REQUESTSTOPTYPING.fields_by_name['typing_type']._options = None
_REQUESTSTOPTYPING._options = None
_REQUESTSETONLINE.fields_by_name['is_online']._options = None
_REQUESTSETONLINE.fields_by_name['timeout']._options = None
_REQUESTSETONLINE.fields_by_name['device_type']._options = None
_REQUESTSETONLINE.fields_by_name['device_category']._options = None
_REQUESTSETONLINE._options = None
_UPDATEPAUSENOTIFICATIONS.fields_by_name['timeout']._options = None
_REQUESTPAUSENOTIFICATIONS.fields_by_name['timeout']._options = None
_REQUESTPAUSENOTIFICATIONS._options = None
_REQUESTRESTORENOTIFICATIONS._options = None
_UPDATETYPING.fields_by_name['peer']._options = None
_UPDATETYPING.fields_by_name['uid']._options = None
_UPDATETYPING.fields_by_name['typing_type']._options = None
_UPDATETYPINGSTOP.fields_by_name['peer']._options = None
_UPDATETYPINGSTOP.fields_by_name['uid']._options = None
_UPDATETYPINGSTOP.fields_by_name['typing_type']._options = None
_UPDATEUSERONLINE.fields_by_name['uid']._options = None
_UPDATEUSEROFFLINE.fields_by_name['uid']._options = None
_UPDATEUSERLASTSEEN.fields_by_name['uid']._options = None
_UPDATEUSERLASTSEEN.fields_by_name['date']._options = None
_UPDATEGROUPONLINE.fields_by_name['group_id']._options = None
_UPDATEGROUPONLINE.fields_by_name['count']._options = None

_TYPINGANDONLINE = _descriptor.ServiceDescriptor(
  name='TypingAndOnline',
  full_name='dialog.TypingAndOnline',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=2078,
  serialized_end=2691,
  methods=[
  _descriptor.MethodDescriptor(
    name='Typing',
    full_name='dialog.TypingAndOnline.Typing',
    index=0,
    containing_service=None,
    input_type=_REQUESTTYPING,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    serialized_options=_b('\202\323\344\223\002$\"\037/v1/grpc/TypingAndOnline/Typing:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='StopTyping',
    full_name='dialog.TypingAndOnline.StopTyping',
    index=1,
    containing_service=None,
    input_type=_REQUESTSTOPTYPING,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    serialized_options=_b('\202\323\344\223\002(\"#/v1/grpc/TypingAndOnline/StopTyping:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='SetOnline',
    full_name='dialog.TypingAndOnline.SetOnline',
    index=2,
    containing_service=None,
    input_type=_REQUESTSETONLINE,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    serialized_options=_b('\202\323\344\223\002\'\"\"/v1/grpc/TypingAndOnline/SetOnline:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='PauseNotifications',
    full_name='dialog.TypingAndOnline.PauseNotifications',
    index=3,
    containing_service=None,
    input_type=_REQUESTPAUSENOTIFICATIONS,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    serialized_options=_b('\202\323\344\223\0020\"+/v1/grpc/TypingAndOnline/PauseNotifications:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='RestoreNotifications',
    full_name='dialog.TypingAndOnline.RestoreNotifications',
    index=4,
    containing_service=None,
    input_type=_REQUESTRESTORENOTIFICATIONS,
    output_type=miscellaneous__pb2._RESPONSEVOID,
    serialized_options=_b('\202\323\344\223\0022\"-/v1/grpc/TypingAndOnline/RestoreNotifications:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_TYPINGANDONLINE)

DESCRIPTOR.services_by_name['TypingAndOnline'] = _TYPINGANDONLINE

# @@protoc_insertion_point(module_scope)
