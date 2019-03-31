# -*- coding: utf-8 -*-
# user = www

import pytest

pytest.main(["--html=Outputs/Reports/pytest_report.html", "--junitxml=Outputs/Reports/report.xml",
             "-m", "smoke", "--reruns", "2", "--alluredir=Outputs/Allures/"])
