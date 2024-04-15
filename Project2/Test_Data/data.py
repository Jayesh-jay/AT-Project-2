class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    before_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/requestPasswordResetCode"
    Username = "Admin"


class login:
    username = "Admin"
    password = "admin123"
    expected_title = "OrangeHRM"
    expected_options = ["User Management", "Job", "Organization", "Qualifications", "Nationalities",
                        "Corporate Branding", "Configuration"]
    main_expected_options = ["Admin", "PIM", "Leave", "Time", "Recruitment", "My Info", "Performance ", "Dashboard",
                             "Directory", "Maintenance", "Claim ", "Buzz"]
