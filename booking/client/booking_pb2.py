# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booking.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\"7\n\x0b\x42ookingData\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0e\n\x06movies\x18\x03 \x03(\t\"\x07\n\x05\x45mpty2a\n\x07\x42ooking\x12-\n\x12GetBookingByUserId\x12\x07.UserId\x1a\x0c.BookingData\"\x00\x12\'\n\x0bGetBookings\x12\x06.Empty\x1a\x0c.BookingData\"\x00\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=17
  _globals['_USERID']._serialized_end=37
  _globals['_BOOKINGDATA']._serialized_start=39
  _globals['_BOOKINGDATA']._serialized_end=94
  _globals['_EMPTY']._serialized_start=96
  _globals['_EMPTY']._serialized_end=103
  _globals['_BOOKING']._serialized_start=105
  _globals['_BOOKING']._serialized_end=202
# @@protoc_insertion_point(module_scope)
