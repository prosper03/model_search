# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
r"""A binary for running and benchmarking the Trainer."""

from absl import app
from absl import flags
from model_search import oss_trainer_lib


if __name__ == "__main__":
  flags.mark_flag_as_required("phoenix_spec_filename")
  app.run(oss_trainer_lib.main)
