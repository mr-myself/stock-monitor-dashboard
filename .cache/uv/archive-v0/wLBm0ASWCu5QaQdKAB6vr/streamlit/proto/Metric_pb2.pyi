"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
*!
Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import streamlit.proto.LabelVisibilityMessage_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class Metric(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _MetricColor:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MetricColorEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Metric._MetricColor.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        RED: Metric._MetricColor.ValueType  # 0
        GREEN: Metric._MetricColor.ValueType  # 1
        GRAY: Metric._MetricColor.ValueType  # 2

    class MetricColor(_MetricColor, metaclass=_MetricColorEnumTypeWrapper): ...
    RED: Metric.MetricColor.ValueType  # 0
    GREEN: Metric.MetricColor.ValueType  # 1
    GRAY: Metric.MetricColor.ValueType  # 2

    class _MetricDirection:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _MetricDirectionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[Metric._MetricDirection.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        DOWN: Metric._MetricDirection.ValueType  # 0
        UP: Metric._MetricDirection.ValueType  # 1
        NONE: Metric._MetricDirection.ValueType  # 2

    class MetricDirection(_MetricDirection, metaclass=_MetricDirectionEnumTypeWrapper): ...
    DOWN: Metric.MetricDirection.ValueType  # 0
    UP: Metric.MetricDirection.ValueType  # 1
    NONE: Metric.MetricDirection.ValueType  # 2

    LABEL_FIELD_NUMBER: builtins.int
    BODY_FIELD_NUMBER: builtins.int
    DELTA_FIELD_NUMBER: builtins.int
    DIRECTION_FIELD_NUMBER: builtins.int
    COLOR_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    LABEL_VISIBILITY_FIELD_NUMBER: builtins.int
    SHOW_BORDER_FIELD_NUMBER: builtins.int
    label: builtins.str
    body: builtins.str
    delta: builtins.str
    direction: global___Metric.MetricDirection.ValueType
    color: global___Metric.MetricColor.ValueType
    help: builtins.str
    show_border: builtins.bool
    @property
    def label_visibility(self) -> streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage: ...
    def __init__(
        self,
        *,
        label: builtins.str = ...,
        body: builtins.str = ...,
        delta: builtins.str = ...,
        direction: global___Metric.MetricDirection.ValueType = ...,
        color: global___Metric.MetricColor.ValueType = ...,
        help: builtins.str = ...,
        label_visibility: streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage | None = ...,
        show_border: builtins.bool = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["label_visibility", b"label_visibility"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["body", b"body", "color", b"color", "delta", b"delta", "direction", b"direction", "help", b"help", "label", b"label", "label_visibility", b"label_visibility", "show_border", b"show_border"]) -> None: ...

global___Metric = Metric
