# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: showtime.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0eshowtime.proto\"\x14\n\x04\x44\x61te\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\",\n\x0cShowtimeData\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\x0e\n\x06movies\x18\x02 \x03(\t\"\x07\n\x05\x45mpty2`\n\x08Showtime\x12+\n\x11GetShowtimeByDate\x12\x05.Date\x1a\r.ShowtimeData\"\x00\x12\'\n\x0cGetShowtimes\x12\x06.Empty\x1a\r.ShowtimeData\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'showtime_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_DATE']._serialized_start=18
  _globals['_DATE']._serialized_end=38
  _globals['_SHOWTIMEDATA']._serialized_start=40
  _globals['_SHOWTIMEDATA']._serialized_end=84
  _globals['_EMPTY']._serialized_start=86
  _globals['_EMPTY']._serialized_end=93
  _globals['_SHOWTIME']._serialized_start=95
  _globals['_SHOWTIME']._serialized_end=191
# @@protoc_insertion_point(module_scope)
