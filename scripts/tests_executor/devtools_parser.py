class DevtoolsParser():
    def parse_histogram(self, obj):
        histogram_dict = {}
        for flutter_frame in obj["performance"]["flutterFrames"]:
            frame_duration = self.parse_frame_info(flutter_frame)
            if frame_duration not in histogram_dict:
                histogram_dict[frame_duration] = 0
            histogram_dict[frame_duration] += 1
        return self.order_dict(histogram_dict)

    def parse_frame_info(self, flutter_frame):
        frame_duration = max(flutter_frame["build"], flutter_frame["raster"])
        frame_duration /= 1000.0
        frame_duration = round(frame_duration)
        return frame_duration

    def order_dict(self, obj):
        return dict(sorted(obj.items(), key=lambda kv: kv[0]))
