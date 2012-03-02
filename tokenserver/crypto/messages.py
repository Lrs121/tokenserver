# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)



DESCRIPTOR = descriptor.FileDescriptor(
  name='tokenserver/crypto/messages.pb',
  package='',
  serialized_pb='\n\x1etokenserver/crypto/messages.pb\"]\n\x0e\x43heckSignature\x12\x10\n\x08hostname\x18\x01 \x02(\t\x12\x13\n\x0bsigned_data\x18\x02 \x02(\t\x12\x11\n\tsignature\x18\x03 \x02(\x0c\x12\x11\n\talgorithm\x18\x04 \x01(\t\"a\n\x16\x43heckSignatureWithCert\x12\x0c\n\x04\x63\x65rt\x18\x01 \x02(\t\x12\x13\n\x0bsigned_data\x18\x02 \x02(\t\x12\x11\n\tsignature\x18\x03 \x02(\x0c\x12\x11\n\talgorithm\x18\x04 \x01(\t\"(\n\x08Response\x12\r\n\x05\x65rror\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x08')




_CHECKSIGNATURE = descriptor.Descriptor(
  name='CheckSignature',
  full_name='CheckSignature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='hostname', full_name='CheckSignature.hostname', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signed_data', full_name='CheckSignature.signed_data', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='CheckSignature.signature', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='algorithm', full_name='CheckSignature.algorithm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=34,
  serialized_end=127,
)


_CHECKSIGNATUREWITHCERT = descriptor.Descriptor(
  name='CheckSignatureWithCert',
  full_name='CheckSignatureWithCert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='cert', full_name='CheckSignatureWithCert.cert', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signed_data', full_name='CheckSignatureWithCert.signed_data', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='signature', full_name='CheckSignatureWithCert.signature', index=2,
      number=3, type=12, cpp_type=9, label=2,
      has_default_value=False, default_value="",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='algorithm', full_name='CheckSignatureWithCert.algorithm', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=129,
  serialized_end=226,
)


_RESPONSE = descriptor.Descriptor(
  name='Response',
  full_name='Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='error', full_name='Response.error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='value', full_name='Response.value', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=228,
  serialized_end=268,
)

DESCRIPTOR.message_types_by_name['CheckSignature'] = _CHECKSIGNATURE
DESCRIPTOR.message_types_by_name['CheckSignatureWithCert'] = _CHECKSIGNATUREWITHCERT
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

class CheckSignature(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKSIGNATURE
  
  # @@protoc_insertion_point(class_scope:CheckSignature)

class CheckSignatureWithCert(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CHECKSIGNATUREWITHCERT
  
  # @@protoc_insertion_point(class_scope:CheckSignatureWithCert)

class Response(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _RESPONSE
  
  # @@protoc_insertion_point(class_scope:Response)

# @@protoc_insertion_point(module_scope)
