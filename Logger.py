class AppLogger:

    def __init__(self, app_config, name):
        self.app_config = app_config
        self.file_name = name

    def write_line(self, obj):
        if self.app_config["run_mode"] != "debug":
            return
        print("%s" % obj)
        f = open(self.file_name, "a")
        f.write("%s" % obj)
        f.write("\n")
        f.close()
