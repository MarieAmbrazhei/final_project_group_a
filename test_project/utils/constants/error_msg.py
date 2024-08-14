class GlobalErrorMsg:

    WRONG_STATUS_CODE = "Wrong Status Code"

    @staticmethod
    def error_msg(exp_code, act_code):
        return f"Expected Status Code: {exp_code} Actual Status Code: {act_code}"
