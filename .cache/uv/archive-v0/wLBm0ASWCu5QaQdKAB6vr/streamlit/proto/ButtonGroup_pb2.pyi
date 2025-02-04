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
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
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
class ButtonGroup(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _ClickMode:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _ClickModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ButtonGroup._ClickMode.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SINGLE_SELECT: ButtonGroup._ClickMode.ValueType  # 0
        MULTI_SELECT: ButtonGroup._ClickMode.ValueType  # 1

    class ClickMode(_ClickMode, metaclass=_ClickModeEnumTypeWrapper): ...
    SINGLE_SELECT: ButtonGroup.ClickMode.ValueType  # 0
    MULTI_SELECT: ButtonGroup.ClickMode.ValueType  # 1

    class _SelectionVisualization:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _SelectionVisualizationEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ButtonGroup._SelectionVisualization.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        ONLY_SELECTED: ButtonGroup._SelectionVisualization.ValueType  # 0
        ALL_UP_TO_SELECTED: ButtonGroup._SelectionVisualization.ValueType  # 1

    class SelectionVisualization(_SelectionVisualization, metaclass=_SelectionVisualizationEnumTypeWrapper): ...
    ONLY_SELECTED: ButtonGroup.SelectionVisualization.ValueType  # 0
    ALL_UP_TO_SELECTED: ButtonGroup.SelectionVisualization.ValueType  # 1

    class _Style:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _StyleEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[ButtonGroup._Style.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        SEGMENTED_CONTROL: ButtonGroup._Style.ValueType  # 0
        PILLS: ButtonGroup._Style.ValueType  # 1
        BORDERLESS: ButtonGroup._Style.ValueType  # 2

    class Style(_Style, metaclass=_StyleEnumTypeWrapper): ...
    SEGMENTED_CONTROL: ButtonGroup.Style.ValueType  # 0
    PILLS: ButtonGroup.Style.ValueType  # 1
    BORDERLESS: ButtonGroup.Style.ValueType  # 2

    @typing.final
    class Option(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        CONTENT_FIELD_NUMBER: builtins.int
        SELECTED_CONTENT_FIELD_NUMBER: builtins.int
        CONTENT_ICON_FIELD_NUMBER: builtins.int
        SELECTED_CONTENT_ICON_FIELD_NUMBER: builtins.int
        content: builtins.str
        selected_content: builtins.str
        """when set, this is the content that will be displayed when the option is selected"""
        content_icon: builtins.str
        """when set, this is the icon that will be displayed next to the option"""
        selected_content_icon: builtins.str
        """when set, this is the icon that will be displayed next to the option when then option is selected"""
        def __init__(
            self,
            *,
            content: builtins.str = ...,
            selected_content: builtins.str | None = ...,
            content_icon: builtins.str | None = ...,
            selected_content_icon: builtins.str | None = ...,
        ) -> None: ...
        def HasField(self, field_name: typing.Literal["_content_icon", b"_content_icon", "_selected_content", b"_selected_content", "_selected_content_icon", b"_selected_content_icon", "content_icon", b"content_icon", "selected_content", b"selected_content", "selected_content_icon", b"selected_content_icon"]) -> builtins.bool: ...
        def ClearField(self, field_name: typing.Literal["_content_icon", b"_content_icon", "_selected_content", b"_selected_content", "_selected_content_icon", b"_selected_content_icon", "content", b"content", "content_icon", b"content_icon", "selected_content", b"selected_content", "selected_content_icon", b"selected_content_icon"]) -> None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing.Literal["_content_icon", b"_content_icon"]) -> typing.Literal["content_icon"] | None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing.Literal["_selected_content", b"_selected_content"]) -> typing.Literal["selected_content"] | None: ...
        @typing.overload
        def WhichOneof(self, oneof_group: typing.Literal["_selected_content_icon", b"_selected_content_icon"]) -> typing.Literal["selected_content_icon"] | None: ...

    ID_FIELD_NUMBER: builtins.int
    OPTIONS_FIELD_NUMBER: builtins.int
    DEFAULT_FIELD_NUMBER: builtins.int
    DISABLED_FIELD_NUMBER: builtins.int
    CLICK_MODE_FIELD_NUMBER: builtins.int
    FORM_ID_FIELD_NUMBER: builtins.int
    VALUE_FIELD_NUMBER: builtins.int
    SET_VALUE_FIELD_NUMBER: builtins.int
    SELECTION_VISUALIZATION_FIELD_NUMBER: builtins.int
    STYLE_FIELD_NUMBER: builtins.int
    LABEL_FIELD_NUMBER: builtins.int
    LABEL_VISIBILITY_FIELD_NUMBER: builtins.int
    HELP_FIELD_NUMBER: builtins.int
    id: builtins.str
    disabled: builtins.bool
    click_mode: global___ButtonGroup.ClickMode.ValueType
    form_id: builtins.str
    set_value: builtins.bool
    selection_visualization: global___ButtonGroup.SelectionVisualization.ValueType
    style: global___ButtonGroup.Style.ValueType
    label: builtins.str
    help: builtins.str
    @property
    def options(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ButtonGroup.Option]: ...
    @property
    def default(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """default is an array of indexes that are selected by default"""

    @property
    def value(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """value passed by the backend"""

    @property
    def label_visibility(self) -> streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage: ...
    def __init__(
        self,
        *,
        id: builtins.str = ...,
        options: collections.abc.Iterable[global___ButtonGroup.Option] | None = ...,
        default: collections.abc.Iterable[builtins.int] | None = ...,
        disabled: builtins.bool = ...,
        click_mode: global___ButtonGroup.ClickMode.ValueType = ...,
        form_id: builtins.str = ...,
        value: collections.abc.Iterable[builtins.int] | None = ...,
        set_value: builtins.bool = ...,
        selection_visualization: global___ButtonGroup.SelectionVisualization.ValueType = ...,
        style: global___ButtonGroup.Style.ValueType = ...,
        label: builtins.str = ...,
        label_visibility: streamlit.proto.LabelVisibilityMessage_pb2.LabelVisibilityMessage | None = ...,
        help: builtins.str | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["_help", b"_help", "help", b"help", "label_visibility", b"label_visibility"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["_help", b"_help", "click_mode", b"click_mode", "default", b"default", "disabled", b"disabled", "form_id", b"form_id", "help", b"help", "id", b"id", "label", b"label", "label_visibility", b"label_visibility", "options", b"options", "selection_visualization", b"selection_visualization", "set_value", b"set_value", "style", b"style", "value", b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["_help", b"_help"]) -> typing.Literal["help"] | None: ...

global___ButtonGroup = ButtonGroup
