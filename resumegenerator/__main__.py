import os
import sys
import json
import shutil
import click
import jinja2


def main():
    """Templated resume generator."""
    input_dir = "../resume"
    output_directory = os.path.join(input_dir, 'resume_result')
    static_directory = os.path.join(input_dir, 'static')
    json_file = os.path.join(input_dir, "config.json")
    template_directory = os.path.join(input_dir, 'templates')

    if os.path.exists(output_directory):
        shutil.rmtree(output_directory)
    if os.path.exists(static_directory):
        shutil.copytree(static_directory, output_directory)
    template_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(template_directory),
        autoescape=jinja2.select_autoescape(['html', 'xml']),)
    config_parameters = json.load(open(json_file))
    for parameter in config_parameters:
        try:
            template_index = template_env.get_template(parameter['template'])
            if not os.path.exists(os.path.join(output_directory + parameter["url"])):
                os.makedirs(os.path.join(output_directory + parameter["url"]))
            result = template_index.render(parameter["context"])
            file = open(os.path.join(output_directory + parameter["url"],
                                     "index.html"), "w")
            file.write(result)
        except IOError:
            sys.exit(1)

if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
