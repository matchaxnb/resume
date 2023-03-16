#!python
import json
import yaml
import sys

class NoDatesSafeLoader(yaml.SafeLoader):
    @classmethod
    def remove_implicit_resolver(cls, tag_to_remove):
        """
        Remove implicit resolvers for a particular tag

        Takes care not to modify resolvers in super classes.

        We want to load datetimes as strings, not dates, because we
        go on to serialise as json which doesn't have the advanced types
        of yaml, and leads to incompatibilities down the track.
        """
        if not 'yaml_implicit_resolvers' in cls.__dict__:
            cls.yaml_implicit_resolvers = cls.yaml_implicit_resolvers.copy()

        for first_letter, mappings in cls.yaml_implicit_resolvers.items():
            cls.yaml_implicit_resolvers[first_letter] = [(tag, regexp) 
                                                         for tag, regexp in mappings
                                                         if tag != tag_to_remove]

NoDatesSafeLoader.remove_implicit_resolver('tag:yaml.org,2002:timestamp')


def main():
    target = sys.argv[1]
    dest = f'{target}.json'
    if len(sys.argv) > 2:
        dest = sys.argv[2]

    data = None
    with open(target, 'r', encoding='utf-8') as f_handler:
        data = yaml.load(f_handler, Loader=NoDatesSafeLoader)

    with open(dest, 'wb') as f_handler:
        json_str = json.dumps(data, indent=4)
        # this avoids writing the BOM
        f_handler.write(json_str.encode('utf-8'))
        

if __name__ == '__main__':
    main()