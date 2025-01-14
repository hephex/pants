# Copyright 2021 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from pants.backend.python.target_types import (
    PythonSourcesGeneratorTarget,
    PythonSourceTarget,
    PythonTestsGeneratorTarget,
    PythonTestTarget,
)
from pants.engine.target import BoolField


class SkipBanditField(BoolField):
    alias = "skip_bandit"
    default = False
    help = "If true, don't run Bandit on this target's code."


def rules():
    return [
        PythonSourceTarget.register_plugin_field(SkipBanditField),
        PythonSourcesGeneratorTarget.register_plugin_field(SkipBanditField),
        PythonTestTarget.register_plugin_field(SkipBanditField),
        PythonTestsGeneratorTarget.register_plugin_field(SkipBanditField),
    ]
