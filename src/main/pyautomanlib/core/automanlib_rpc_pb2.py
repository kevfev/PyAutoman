# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: automanlib_rpc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import automanlib_wrappers_pb2 as automanlib__wrappers__pb2
import automanlib_classes_pb2 as automanlib__classes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='automanlib_rpc.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x14\x61utomanlib_rpc.proto\x1a\x19\x61utomanlib_wrappers.proto\x1a\x18\x61utomanlib_classes.proto\"\xcb\x02\n\x0b\x41utomanTask\x12!\n\x08\x65stimate\x18\x01 \x01(\x0b\x32\r.EstimateTaskH\x00\x12+\n\rmultiestimate\x18\x02 \x01(\x0b\x32\x12.MultiestimateTaskH\x00\x12!\n\x08\x66reetext\x18\x03 \x01(\x0b\x32\r.FreetextTaskH\x00\x12*\n\rfreetext_dist\x18\x04 \x01(\x0b\x32\x11.FreetextDistTaskH\x00\x12\x1b\n\x05radio\x18\x05 \x01(\x0b\x32\n.RadioTaskH\x00\x12$\n\nradio_dist\x18\x06 \x01(\x0b\x32\x0e.RadioDistTaskH\x00\x12!\n\x08\x63heckbox\x18\x07 \x01(\x0b\x32\r.CheckboxTaskH\x00\x12*\n\rcheckbox_dist\x18\x08 \x01(\x0b\x32\x11.CheckboxDistTaskH\x00\x42\x0b\n\ttask_type\"\x9e\x06\n\x0cTaskResponse\x12\x31\n\x0breturn_code\x18\x01 \x01(\x0e\x32\x1c.TaskResponse.TaskReturnCode\x12,\n\x10\x65stimate_outcome\x18\x02 \x01(\x0b\x32\x10.EstimateOutcomeH\x00\x12\x36\n\x15multiestimate_outcome\x18\x03 \x01(\x0b\x32\x15.MultiestimateOutcomeH\x00\x12&\n\rradio_outcome\x18\x04 \x01(\x0b\x32\r.RadioOutcomeH\x00\x12/\n\x12radio_dist_outcome\x18\x05 \x01(\x0b\x32\x11.RadioDistOutcomeH\x00\x12,\n\x10\x66reetext_outcome\x18\x06 \x01(\x0b\x32\x10.FreetextOutcomeH\x00\x12\x35\n\x15\x66reetext_dist_outcome\x18\x07 \x01(\x0b\x32\x14.FreetextDistOutcomeH\x00\x12,\n\x10\x63heckbox_outcome\x18\x08 \x01(\x0b\x32\x10.CheckboxOutcomeH\x00\x12\x35\n\x15\x63heckbox_dist_outcome\x18\t \x01(\x0b\x32\x14.CheckboxDistOutcomeH\x00\x12/\n\nexcep_code\x18\x10 \x01(\x0e\x32\x1b.TaskResponse.ExceptionCode\x12)\n\x08\x65rr_code\x18\x11 \x01(\x0e\x32\x17.TaskResponse.ErrorCode\x12\x0f\n\x07\x65rr_msg\x18\x12 \x01(\t\x12\x11\n\texcep_msg\x18\x13 \x01(\t\"N\n\x0eTaskReturnCode\x12\x17\n\x13UNDEFINED_RESP_CODE\x10\x00\x12\t\n\x05VALID\x10\x01\x12\t\n\x05\x45RROR\x10\x02\x12\r\n\tEXCEPTION\x10\x03\",\n\rExceptionCode\x12\x1b\n\x17UNDEFINED_EXCPTION_CODE\x10\x00\"D\n\tErrorCode\x12\x18\n\x14UNDEFINED_ERROR_CODE\x10\x00\x12\x1d\n\x19NO_CREDENTIALS_REGISTERED\x10\x01\x42\x0e\n\x0ctask_outcome\"\x9c\x01\n\x14RegistrationResponse\x12\x38\n\x0breturn_code\x18\x01 \x01(\x0e\x32#.RegistrationResponse.RegReturnCode\x12\x0f\n\x07\x65rr_msg\x18\x02 \x01(\t\"9\n\rRegReturnCode\x12\x12\n\x0eUNDEFINED_CODE\x10\x00\x12\x08\n\x04OKAY\x10\x01\x12\n\n\x06\x46\x41ILED\x10\x02\"\x97\x01\n\x14ServerStatusResponse\x12\x39\n\x0breturn_code\x18\x01 \x01(\x0e\x32$.ServerStatusResponse.StatReturnCode\"D\n\x0eStatReturnCode\x12\x19\n\x15UNDEFINED_STATUS_CODE\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06KILLED\x10\x02\"\x07\n\x05\x45mpty2\xe3\x01\n\x13\x45stimationPrototype\x12-\n\nKillServer\x12\x06.Empty\x1a\x15.ServerStatusResponse\"\x00\x12?\n\x0fRegisterAdapter\x12\x13.AdapterCredentials\x1a\x15.RegistrationResponse\"\x00\x12+\n\nSubmitTask\x12\x0c.AutomanTask\x1a\r.TaskResponse\"\x00\x12/\n\x0cServerStatus\x12\x06.Empty\x1a\x15.ServerStatusResponse\"\x00\x62\x06proto3')
  ,
  dependencies=[automanlib__wrappers__pb2.DESCRIPTOR,automanlib__classes__pb2.DESCRIPTOR,])



_TASKRESPONSE_TASKRETURNCODE = _descriptor.EnumDescriptor(
  name='TaskReturnCode',
  full_name='TaskResponse.TaskReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_RESP_CODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALID', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ERROR', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EXCEPTION', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1000,
  serialized_end=1078,
)
_sym_db.RegisterEnumDescriptor(_TASKRESPONSE_TASKRETURNCODE)

_TASKRESPONSE_EXCEPTIONCODE = _descriptor.EnumDescriptor(
  name='ExceptionCode',
  full_name='TaskResponse.ExceptionCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_EXCPTION_CODE', index=0, number=0,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1080,
  serialized_end=1124,
)
_sym_db.RegisterEnumDescriptor(_TASKRESPONSE_EXCEPTIONCODE)

_TASKRESPONSE_ERRORCODE = _descriptor.EnumDescriptor(
  name='ErrorCode',
  full_name='TaskResponse.ErrorCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_ERROR_CODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NO_CREDENTIALS_REGISTERED', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1126,
  serialized_end=1194,
)
_sym_db.RegisterEnumDescriptor(_TASKRESPONSE_ERRORCODE)

_REGISTRATIONRESPONSE_REGRETURNCODE = _descriptor.EnumDescriptor(
  name='RegReturnCode',
  full_name='RegistrationResponse.RegReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_CODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OKAY', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FAILED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1312,
  serialized_end=1369,
)
_sym_db.RegisterEnumDescriptor(_REGISTRATIONRESPONSE_REGRETURNCODE)

_SERVERSTATUSRESPONSE_STATRETURNCODE = _descriptor.EnumDescriptor(
  name='StatReturnCode',
  full_name='ServerStatusResponse.StatReturnCode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNDEFINED_STATUS_CODE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='KILLED', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1455,
  serialized_end=1523,
)
_sym_db.RegisterEnumDescriptor(_SERVERSTATUSRESPONSE_STATRETURNCODE)


_AUTOMANTASK = _descriptor.Descriptor(
  name='AutomanTask',
  full_name='AutomanTask',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='estimate', full_name='AutomanTask.estimate', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiestimate', full_name='AutomanTask.multiestimate', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freetext', full_name='AutomanTask.freetext', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freetext_dist', full_name='AutomanTask.freetext_dist', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio', full_name='AutomanTask.radio', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio_dist', full_name='AutomanTask.radio_dist', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkbox', full_name='AutomanTask.checkbox', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkbox_dist', full_name='AutomanTask.checkbox_dist', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='task_type', full_name='AutomanTask.task_type',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=78,
  serialized_end=409,
)


_TASKRESPONSE = _descriptor.Descriptor(
  name='TaskResponse',
  full_name='TaskResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='TaskResponse.return_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='estimate_outcome', full_name='TaskResponse.estimate_outcome', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='multiestimate_outcome', full_name='TaskResponse.multiestimate_outcome', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio_outcome', full_name='TaskResponse.radio_outcome', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='radio_dist_outcome', full_name='TaskResponse.radio_dist_outcome', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freetext_outcome', full_name='TaskResponse.freetext_outcome', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freetext_dist_outcome', full_name='TaskResponse.freetext_dist_outcome', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkbox_outcome', full_name='TaskResponse.checkbox_outcome', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='checkbox_dist_outcome', full_name='TaskResponse.checkbox_dist_outcome', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excep_code', full_name='TaskResponse.excep_code', index=9,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_code', full_name='TaskResponse.err_code', index=10,
      number=17, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='TaskResponse.err_msg', index=11,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='excep_msg', full_name='TaskResponse.excep_msg', index=12,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _TASKRESPONSE_TASKRETURNCODE,
    _TASKRESPONSE_EXCEPTIONCODE,
    _TASKRESPONSE_ERRORCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='task_outcome', full_name='TaskResponse.task_outcome',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=412,
  serialized_end=1210,
)


_REGISTRATIONRESPONSE = _descriptor.Descriptor(
  name='RegistrationResponse',
  full_name='RegistrationResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='RegistrationResponse.return_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='err_msg', full_name='RegistrationResponse.err_msg', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _REGISTRATIONRESPONSE_REGRETURNCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1213,
  serialized_end=1369,
)


_SERVERSTATUSRESPONSE = _descriptor.Descriptor(
  name='ServerStatusResponse',
  full_name='ServerStatusResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='return_code', full_name='ServerStatusResponse.return_code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _SERVERSTATUSRESPONSE_STATRETURNCODE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1372,
  serialized_end=1523,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='Empty',
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1525,
  serialized_end=1532,
)

_AUTOMANTASK.fields_by_name['estimate'].message_type = automanlib__wrappers__pb2._ESTIMATETASK
_AUTOMANTASK.fields_by_name['multiestimate'].message_type = automanlib__wrappers__pb2._MULTIESTIMATETASK
_AUTOMANTASK.fields_by_name['freetext'].message_type = automanlib__wrappers__pb2._FREETEXTTASK
_AUTOMANTASK.fields_by_name['freetext_dist'].message_type = automanlib__wrappers__pb2._FREETEXTDISTTASK
_AUTOMANTASK.fields_by_name['radio'].message_type = automanlib__wrappers__pb2._RADIOTASK
_AUTOMANTASK.fields_by_name['radio_dist'].message_type = automanlib__wrappers__pb2._RADIODISTTASK
_AUTOMANTASK.fields_by_name['checkbox'].message_type = automanlib__wrappers__pb2._CHECKBOXTASK
_AUTOMANTASK.fields_by_name['checkbox_dist'].message_type = automanlib__wrappers__pb2._CHECKBOXDISTTASK
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['estimate'])
_AUTOMANTASK.fields_by_name['estimate'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['multiestimate'])
_AUTOMANTASK.fields_by_name['multiestimate'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['freetext'])
_AUTOMANTASK.fields_by_name['freetext'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['freetext_dist'])
_AUTOMANTASK.fields_by_name['freetext_dist'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['radio'])
_AUTOMANTASK.fields_by_name['radio'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['radio_dist'])
_AUTOMANTASK.fields_by_name['radio_dist'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['checkbox'])
_AUTOMANTASK.fields_by_name['checkbox'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_AUTOMANTASK.oneofs_by_name['task_type'].fields.append(
  _AUTOMANTASK.fields_by_name['checkbox_dist'])
_AUTOMANTASK.fields_by_name['checkbox_dist'].containing_oneof = _AUTOMANTASK.oneofs_by_name['task_type']
_TASKRESPONSE.fields_by_name['return_code'].enum_type = _TASKRESPONSE_TASKRETURNCODE
_TASKRESPONSE.fields_by_name['estimate_outcome'].message_type = automanlib__wrappers__pb2._ESTIMATEOUTCOME
_TASKRESPONSE.fields_by_name['multiestimate_outcome'].message_type = automanlib__wrappers__pb2._MULTIESTIMATEOUTCOME
_TASKRESPONSE.fields_by_name['radio_outcome'].message_type = automanlib__wrappers__pb2._RADIOOUTCOME
_TASKRESPONSE.fields_by_name['radio_dist_outcome'].message_type = automanlib__wrappers__pb2._RADIODISTOUTCOME
_TASKRESPONSE.fields_by_name['freetext_outcome'].message_type = automanlib__wrappers__pb2._FREETEXTOUTCOME
_TASKRESPONSE.fields_by_name['freetext_dist_outcome'].message_type = automanlib__wrappers__pb2._FREETEXTDISTOUTCOME
_TASKRESPONSE.fields_by_name['checkbox_outcome'].message_type = automanlib__wrappers__pb2._CHECKBOXOUTCOME
_TASKRESPONSE.fields_by_name['checkbox_dist_outcome'].message_type = automanlib__wrappers__pb2._CHECKBOXDISTOUTCOME
_TASKRESPONSE.fields_by_name['excep_code'].enum_type = _TASKRESPONSE_EXCEPTIONCODE
_TASKRESPONSE.fields_by_name['err_code'].enum_type = _TASKRESPONSE_ERRORCODE
_TASKRESPONSE_TASKRETURNCODE.containing_type = _TASKRESPONSE
_TASKRESPONSE_EXCEPTIONCODE.containing_type = _TASKRESPONSE
_TASKRESPONSE_ERRORCODE.containing_type = _TASKRESPONSE
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['estimate_outcome'])
_TASKRESPONSE.fields_by_name['estimate_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['multiestimate_outcome'])
_TASKRESPONSE.fields_by_name['multiestimate_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['radio_outcome'])
_TASKRESPONSE.fields_by_name['radio_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['radio_dist_outcome'])
_TASKRESPONSE.fields_by_name['radio_dist_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['freetext_outcome'])
_TASKRESPONSE.fields_by_name['freetext_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['freetext_dist_outcome'])
_TASKRESPONSE.fields_by_name['freetext_dist_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['checkbox_outcome'])
_TASKRESPONSE.fields_by_name['checkbox_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_TASKRESPONSE.oneofs_by_name['task_outcome'].fields.append(
  _TASKRESPONSE.fields_by_name['checkbox_dist_outcome'])
_TASKRESPONSE.fields_by_name['checkbox_dist_outcome'].containing_oneof = _TASKRESPONSE.oneofs_by_name['task_outcome']
_REGISTRATIONRESPONSE.fields_by_name['return_code'].enum_type = _REGISTRATIONRESPONSE_REGRETURNCODE
_REGISTRATIONRESPONSE_REGRETURNCODE.containing_type = _REGISTRATIONRESPONSE
_SERVERSTATUSRESPONSE.fields_by_name['return_code'].enum_type = _SERVERSTATUSRESPONSE_STATRETURNCODE
_SERVERSTATUSRESPONSE_STATRETURNCODE.containing_type = _SERVERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['AutomanTask'] = _AUTOMANTASK
DESCRIPTOR.message_types_by_name['TaskResponse'] = _TASKRESPONSE
DESCRIPTOR.message_types_by_name['RegistrationResponse'] = _REGISTRATIONRESPONSE
DESCRIPTOR.message_types_by_name['ServerStatusResponse'] = _SERVERSTATUSRESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AutomanTask = _reflection.GeneratedProtocolMessageType('AutomanTask', (_message.Message,), dict(
  DESCRIPTOR = _AUTOMANTASK,
  __module__ = 'automanlib_rpc_pb2'
  # @@protoc_insertion_point(class_scope:AutomanTask)
  ))
_sym_db.RegisterMessage(AutomanTask)

TaskResponse = _reflection.GeneratedProtocolMessageType('TaskResponse', (_message.Message,), dict(
  DESCRIPTOR = _TASKRESPONSE,
  __module__ = 'automanlib_rpc_pb2'
  # @@protoc_insertion_point(class_scope:TaskResponse)
  ))
_sym_db.RegisterMessage(TaskResponse)

RegistrationResponse = _reflection.GeneratedProtocolMessageType('RegistrationResponse', (_message.Message,), dict(
  DESCRIPTOR = _REGISTRATIONRESPONSE,
  __module__ = 'automanlib_rpc_pb2'
  # @@protoc_insertion_point(class_scope:RegistrationResponse)
  ))
_sym_db.RegisterMessage(RegistrationResponse)

ServerStatusResponse = _reflection.GeneratedProtocolMessageType('ServerStatusResponse', (_message.Message,), dict(
  DESCRIPTOR = _SERVERSTATUSRESPONSE,
  __module__ = 'automanlib_rpc_pb2'
  # @@protoc_insertion_point(class_scope:ServerStatusResponse)
  ))
_sym_db.RegisterMessage(ServerStatusResponse)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'automanlib_rpc_pb2'
  # @@protoc_insertion_point(class_scope:Empty)
  ))
_sym_db.RegisterMessage(Empty)



_ESTIMATIONPROTOTYPE = _descriptor.ServiceDescriptor(
  name='EstimationPrototype',
  full_name='EstimationPrototype',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=1535,
  serialized_end=1762,
  methods=[
  _descriptor.MethodDescriptor(
    name='KillServer',
    full_name='EstimationPrototype.KillServer',
    index=0,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_SERVERSTATUSRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RegisterAdapter',
    full_name='EstimationPrototype.RegisterAdapter',
    index=1,
    containing_service=None,
    input_type=automanlib__classes__pb2._ADAPTERCREDENTIALS,
    output_type=_REGISTRATIONRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubmitTask',
    full_name='EstimationPrototype.SubmitTask',
    index=2,
    containing_service=None,
    input_type=_AUTOMANTASK,
    output_type=_TASKRESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerStatus',
    full_name='EstimationPrototype.ServerStatus',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_SERVERSTATUSRESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ESTIMATIONPROTOTYPE)

DESCRIPTOR.services_by_name['EstimationPrototype'] = _ESTIMATIONPROTOTYPE

# @@protoc_insertion_point(module_scope)
