d = {
    "name":"Hrithik",
    "uid" :{
        "admision_no":"20ec051",
        "roll_no":"20009..79",
        "class":{
            "num":8,
            "section":"ec2"
        }
    }
}
d2 = {}
def flatten_dict(d, parent_key='', sep='_'):
    for k, v in d.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            flatten_dict(v, new_key, sep=sep)
        else:
            d2[new_key] = v

flatten_dict(d)
    