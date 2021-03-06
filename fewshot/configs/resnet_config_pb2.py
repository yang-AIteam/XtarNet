# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: fewshot/configs/resnet_config.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='fewshot/configs/resnet_config.proto',
  package='fewshot.configs',
  serialized_pb=_b('\n#fewshot/configs/resnet_config.proto\x12\x0f\x66\x65wshot.configs\"\xc9\x03\n\x0cResnetConfig\x12\x0e\n\x06height\x18\x01 \x01(\x05\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x13\n\x0bnum_channel\x18\x03 \x01(\x05\x12\x1a\n\x12num_residual_units\x18\x04 \x03(\x05\x12\x13\n\x0bnum_filters\x18\x05 \x03(\x05\x12\x0f\n\x07strides\x18\x06 \x03(\x05\x12\x13\n\x0binit_stride\x18\x07 \x01(\x05\x12\x15\n\rinit_max_pool\x18\x08 \x01(\x08\x12\x13\n\x0binit_filter\x18\t \x01(\x05\x12\x16\n\x0euse_bottleneck\x18\n \x01(\x08\x12\n\n\x02wd\x18\x0b \x01(\x02\x12!\n\rnormalization\x18\x0c \x01(\t:\nbatch_norm\x12\x17\n\x0fnum_norm_groups\x18\r \x01(\x05\x12\x17\n\x0fglobal_avg_pool\x18\x0e \x01(\x08\x12\x19\n\x0b\x64\x61ta_format\x18\x0f \x01(\t:\x04NCHW\x12\x13\n\x07version\x18\x10 \x01(\t:\x02v1\x12\x15\n\nleaky_relu\x18\x11 \x01(\x02:\x01\x30\x12%\n\x15\x66ilter_initialization\x18\x12 \x01(\t:\x06normal\x12\x1b\n\radd_last_relu\x18\x13 \x01(\x08:\x04true')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESNETCONFIG = _descriptor.Descriptor(
  name='ResnetConfig',
  full_name='fewshot.configs.ResnetConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='height', full_name='fewshot.configs.ResnetConfig.height', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='width', full_name='fewshot.configs.ResnetConfig.width', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_channel', full_name='fewshot.configs.ResnetConfig.num_channel', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_residual_units', full_name='fewshot.configs.ResnetConfig.num_residual_units', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_filters', full_name='fewshot.configs.ResnetConfig.num_filters', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='strides', full_name='fewshot.configs.ResnetConfig.strides', index=5,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_stride', full_name='fewshot.configs.ResnetConfig.init_stride', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_max_pool', full_name='fewshot.configs.ResnetConfig.init_max_pool', index=7,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='init_filter', full_name='fewshot.configs.ResnetConfig.init_filter', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='use_bottleneck', full_name='fewshot.configs.ResnetConfig.use_bottleneck', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wd', full_name='fewshot.configs.ResnetConfig.wd', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='normalization', full_name='fewshot.configs.ResnetConfig.normalization', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("batch_norm").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_norm_groups', full_name='fewshot.configs.ResnetConfig.num_norm_groups', index=12,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='global_avg_pool', full_name='fewshot.configs.ResnetConfig.global_avg_pool', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='data_format', full_name='fewshot.configs.ResnetConfig.data_format', index=14,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("NCHW").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='fewshot.configs.ResnetConfig.version', index=15,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("v1").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='leaky_relu', full_name='fewshot.configs.ResnetConfig.leaky_relu', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='filter_initialization', full_name='fewshot.configs.ResnetConfig.filter_initialization', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("normal").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='add_last_relu', full_name='fewshot.configs.ResnetConfig.add_last_relu', index=18,
      number=19, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  oneofs=[
  ],
  serialized_start=57,
  serialized_end=514,
)

DESCRIPTOR.message_types_by_name['ResnetConfig'] = _RESNETCONFIG

ResnetConfig = _reflection.GeneratedProtocolMessageType('ResnetConfig', (_message.Message,), dict(
  DESCRIPTOR = _RESNETCONFIG,
  __module__ = 'fewshot.configs.resnet_config_pb2'
  # @@protoc_insertion_point(class_scope:fewshot.configs.ResnetConfig)
  ))
_sym_db.RegisterMessage(ResnetConfig)


# @@protoc_insertion_point(module_scope)
