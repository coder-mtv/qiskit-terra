# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""The diagonal gate.

This module is deprecated, see diagonal.py
"""

import warnings
# pylint: disable=unused-import
from qiskit.extensions.quantum_initializer.diagonal import DiagGate, diag_gate

warnings.warn('This module is deprecated. The DiagonalGate/DiagGate is now in diagonal.py',
              category=DeprecationWarning, stacklevel=2)
