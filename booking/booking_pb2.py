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




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\"\x14\n\x06UserId\x12\n\n\x02id\x18\x01 \x01(\t\";\n\x0e\x42ookingRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0f\n\x07movieid\x18\x03 \x01(\t\";\n\x0f\x42ookingResponse\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\x12\x0e\n\x06movies\x18\x03 \x03(\t\"\x0e\n\x0c\x42ookingEmpty2\xa8\x01\n\x07\x42ooking\x12\x33\n\x12GetBookingByUserId\x12\x07.UserId\x1a\x10.BookingResponse\"\x00\x30\x01\x12\x32\n\x0bGetBookings\x12\r.BookingEmpty\x1a\x10.BookingResponse\"\x00\x30\x01\x12\x34\n\rCreateBooking\x12\x0f.BookingRequest\x1a\x10.BookingResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_USERID']._serialized_start=17
  _globals['_USERID']._serialized_end=37
  _globals['_BOOKINGREQUEST']._serialized_start=39
  _globals['_BOOKINGREQUEST']._serialized_end=98
  _globals['_BOOKINGRESPONSE']._serialized_start=100
  _globals['_BOOKINGRESPONSE']._serialized_end=159
  _globals['_BOOKINGEMPTY']._serialized_start=161
  _globals['_BOOKINGEMPTY']._serialized_end=175
  _globals['_BOOKING']._serialized_start=178
  _globals['_BOOKING']._serialized_end=346
# @@protoc_insertion_point(module_scope)
