################################################################################
#  Licensed to the Apache Software Foundation (ASF) under one
#  or more contributor license agreements.  See the NOTICE file
#  distributed with this work for additional information
#  regarding copyright ownership.  The ASF licenses this file
#  to you under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
#################################################################################
from abc import ABC, abstractmethod
from typing import Any, Dict


class AgentRunner(ABC):
    """Abstract base class defining the interface for agent execution.

    Concrete implementations must implement the `run` method to handle agent
    execution logic specific to their use case.
    """

    @abstractmethod
    def run(self, **data: Dict[str, Any]) -> Any:
        """Execute the agent and return the key of input.

        Parameters
        ----------
        **data : dict[str, Any]
            input record from upstream.

        Returns:
        -------
        Any
            The key of the input that was processed, will be automatically
            generated if necessary.
        """

