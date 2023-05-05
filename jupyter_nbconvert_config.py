# Configuration file for jupyter-nbconvert.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------
## Base class for Jupyter applications

## Answer yes to any prompts.
#  Default: False
# c.JupyterApp.answer_yes = False

## Full path of a config file.
#  Default: ''
# c.JupyterApp.config_file = ''

## Specify a config file to load.
#  Default: ''
# c.JupyterApp.config_file_name = ''

## Generate default config file.
#  Default: False
# c.JupyterApp.generate_config = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.JupyterApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.JupyterApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.JupyterApp.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.JupyterApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.JupyterApp.show_config_json = False

#------------------------------------------------------------------------------
# NbConvertApp(JupyterApp) configuration
#------------------------------------------------------------------------------
## This application is used to convert notebook files (*.ipynb) to various other
#  formats.
#  
#  WARNING: THE COMMANDLINE INTERFACE MAY CHANGE IN FUTURE RELEASES.

## Answer yes to any prompts.
#  See also: JupyterApp.answer_yes
# c.NbConvertApp.answer_yes = False

## Full path of a config file.
#  See also: JupyterApp.config_file
# c.NbConvertApp.config_file = ''

## Specify a config file to load.
#  See also: JupyterApp.config_file_name
# c.NbConvertApp.config_file_name = ''

## The export format to be used, either one of the built-in formats ['asciidoc',
#  'custom', 'html', 'latex', 'markdown', 'notebook', 'pdf', 'python', 'rst',
#  'script', 'slides', 'webpdf'] or a dotted object name that represents the
#  import path for an `Exporter` class
#  Default: ''
c.NbConvertApp.export_format = 'latex'

## read a single notebook from stdin.
#  Default: False
# c.NbConvertApp.from_stdin = False

## Generate default config file.
#  See also: JupyterApp.generate_config
# c.NbConvertApp.generate_config = False

## Semver range for Jupyter widgets HTML manager
#  Default: '*'
# c.NbConvertApp.html_manager_semver_range = '*'

## URL base for Jupyter widgets
#  Default: 'https://unpkg.com/'
# c.NbConvertApp.jupyter_widgets_base_url = 'https://unpkg.com/'

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.NbConvertApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.NbConvertApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.NbConvertApp.log_level = 30

## List of notebooks to convert. Wildcards are supported. Filenames passed
#  positionally will be added to the list.
#  Default: []
# c.NbConvertApp.notebooks = []

## overwrite base name use for output files. can only be used when converting one
#  notebook at a time.
#  Default: ''
# c.NbConvertApp.output_base = ''

## Directory to copy extra files (figures) to. '{notebook_name}' in the string
#  will be converted to notebook basename.
#  Default: '{notebook_name}_files'
# c.NbConvertApp.output_files_dir = '{notebook_name}_files'

## PostProcessor class used to write the results of the conversion
#  Default: ''
# c.NbConvertApp.postprocessor_class = ''

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.NbConvertApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.NbConvertApp.show_config_json = False

## Whether to apply a suffix prior to the extension (only relevant when
#  converting to notebook format). The suffix is determined by the exporter, and
#  is usually '.nbconvert'.
#  Default: True
# c.NbConvertApp.use_output_suffix = True

## Writer class used to write the  results of the conversion
#  Default: 'FilesWriter'
# c.NbConvertApp.writer_class = 'FilesWriter'

#------------------------------------------------------------------------------
# NbConvertBase(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Global configurable class for shared config
#  
#  Useful for display data priority that might be used by many transformers

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  Default: 'ipython'
# c.NbConvertBase.default_language = 'ipython'

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']
# c.NbConvertBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#------------------------------------------------------------------------------
# Exporter(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Class containing methods that sequentially run a list of preprocessors on a
#  NotebookNode object and then return the modified NotebookNode object and
#  accompanying resources dict.

## List of preprocessors available by default, by name, namespace, instance, or
#  type.
#  Default: ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']
# c.Exporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  Default: True
# c.Exporter.enabled = True

## Extension of the file that should be written to disk
#  Default: ''
# c.Exporter.file_extension = ''

## List of preprocessors, by name or namespace, to enable.
#  Default: []
# c.Exporter.preprocessors = []

#------------------------------------------------------------------------------
# TemplateExporter(Exporter) configuration
#------------------------------------------------------------------------------
## Exports notebooks into other file formats.  Uses Jinja 2 templating engine to
#  output new formats.  Inherit from this class if you are creating a new
#  template type along with new filters/preprocessors.  If the filters/
#  preprocessors provided by default suffice, there is no need to inherit from
#  this class.  Instead, override the template_file and file_extension traits via
#  a config file.
#  
#  Filters available by default for templates:
#  
#  - add_anchor - add_prompts - ansi2html - ansi2latex - ascii_only -
#  citation2latex - comment_lines - convert_pandoc - escape_latex -
#  filter_data_type - get_lines - get_metadata - highlight2html - highlight2latex
#  - html2text - indent - ipython2python - json_dumps - markdown2asciidoc -
#  markdown2html - markdown2latex - markdown2rst - path2url - posix_path -
#  prevent_list_blocks - strip_ansi - strip_dollars - strip_files_prefix -
#  strip_trailing_newline - wrap_text

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.TemplateExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.TemplateExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  Default: False
# c.TemplateExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  Default: False
# c.TemplateExporter.exclude_unknown = False

#  Default: []
# c.TemplateExporter.extra_template_basedirs = []

#  Default: []
# c.TemplateExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.TemplateExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja environment.
#  Default: {}
# c.TemplateExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.TemplateExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  Default: []
# c.TemplateExporter.raw_mimetypes = []

#  Default: ''
# c.TemplateExporter.template_extension = ''

## Name of the template file to use
#  Default: None
# c.TemplateExporter.template_file = None

## Name of the template to use
#  Default: ''
# c.TemplateExporter.template_name = ''

#  Default: ['.']
# c.TemplateExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# ASCIIDocExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports to an ASCIIDoc document (.asciidoc)

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.ASCIIDocExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.ASCIIDocExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.ASCIIDocExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.ASCIIDocExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.ASCIIDocExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.ASCIIDocExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.ASCIIDocExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.ASCIIDocExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.ASCIIDocExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.ASCIIDocExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.ASCIIDocExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.ASCIIDocExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.ASCIIDocExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.ASCIIDocExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.ASCIIDocExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.ASCIIDocExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.ASCIIDocExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.ASCIIDocExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.ASCIIDocExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.ASCIIDocExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# HTMLExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports a basic HTML document.  This exporter assists with the export of HTML.
#  Inherit from it if you are writing your own HTML template and need custom
#  preprocessors/filters.  If you don't need custom preprocessors/ filters, just
#  change the 'template_file' config option.

## The text used as the text for anchor links.
#  Default: '¶'
# c.HTMLExporter.anchor_link_text = '¶'

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.HTMLExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.HTMLExporter.enabled = True

## If anchor links should be included or not.
#  Default: False
# c.HTMLExporter.exclude_anchor_links = False

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.HTMLExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.HTMLExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.HTMLExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.HTMLExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.HTMLExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.HTMLExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.HTMLExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.HTMLExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.HTMLExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.HTMLExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.HTMLExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.HTMLExporter.filters = {}

## URL to load jQuery from.
#  
#  Defaults to loading from cdnjs.
#  Default: 'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js'
# c.HTMLExporter.jquery_url = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js'

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.HTMLExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.HTMLExporter.raw_mimetypes = []

## URL to load require.js from.
#  
#  Defaults to loading from cdnjs.
#  Default: 'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js'
# c.HTMLExporter.require_js_url = 'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js'

#  See also: TemplateExporter.template_extension
# c.HTMLExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.HTMLExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.HTMLExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.HTMLExporter.template_paths = ['.']

## Template specific theme(e.g. the JupyterLab CSS theme for the lab template)
#  Default: 'light'
# c.HTMLExporter.theme = 'light'

#------------------------------------------------------------------------------
# LatexExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports to a Latex template.  Inherit from this class if your template is
#  LaTeX based and you need custom transformers/filters. If you don't need custom
#  transformers/filters, just change the  'template_file' config option.  Place
#  your template in the special "/latex"  subfolder of the "../templates" folder.

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.LatexExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.LatexExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.LatexExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.LatexExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.LatexExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.LatexExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.LatexExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.LatexExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.LatexExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.LatexExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.LatexExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
c.LatexExporter.extra_template_paths = ['/home/richard/.local/share/jupyter/nbconvert/templates/latex']

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.LatexExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.LatexExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.LatexExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.LatexExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.LatexExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.LatexExporter.template_file = ''

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.LatexExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.LatexExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# MarkdownExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports to a markdown document (.md)

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.MarkdownExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.MarkdownExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.MarkdownExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.MarkdownExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.MarkdownExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.MarkdownExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.MarkdownExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.MarkdownExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.MarkdownExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.MarkdownExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.MarkdownExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.MarkdownExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.MarkdownExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.MarkdownExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.MarkdownExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.MarkdownExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.MarkdownExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.MarkdownExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.MarkdownExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.MarkdownExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# NotebookExporter(Exporter) configuration
#------------------------------------------------------------------------------
## Exports to an IPython notebook.
#  
#  This is useful when you want to use nbconvert's preprocessors to operate on a
#  notebook (e.g. to execute it) and then write it back to a notebook file.

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.NotebookExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.NotebookExporter.enabled = True

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.NotebookExporter.file_extension = ''

## The nbformat version to write. Use this to downgrade notebooks.
#  Choices: any of [1, 2, 3, 4]
#  Default: 4
# c.NotebookExporter.nbformat_version = 4

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.NotebookExporter.preprocessors = []

#------------------------------------------------------------------------------
# PDFExporter(LatexExporter) configuration
#------------------------------------------------------------------------------
## Writer designed to write to PDF files.
#  
#  This inherits from `LatexExporter`. It creates a LaTeX file in a temporary
#  directory using the template machinery, and then runs LaTeX to create a pdf.

## Shell command used to run bibtex.
#  Default: ['bibtex', '{filename}']
# c.PDFExporter.bib_command = ['bibtex', '{filename}']

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.PDFExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.PDFExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.PDFExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.PDFExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.PDFExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.PDFExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.PDFExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.PDFExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.PDFExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.PDFExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.PDFExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.PDFExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.PDFExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.PDFExporter.filters = {}

## Shell command used to compile latex.
#  Default: ['xelatex', '{filename}', '-quiet']
# c.PDFExporter.latex_command = ['xelatex', '{filename}', '-quiet']

## How many times latex will be called.
#  Default: 3
# c.PDFExporter.latex_count = 3

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.PDFExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.PDFExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.PDFExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.PDFExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.PDFExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.PDFExporter.template_paths = ['.']

## Whether to display the output of latex commands.
#  Default: False
# c.PDFExporter.verbose = False

#------------------------------------------------------------------------------
# PythonExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports a Python code file. Note that the file produced will have a shebang of
#  '#!/usr/bin/env python' regardless of the actual python version used in the
#  notebook.

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.PythonExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.PythonExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.PythonExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.PythonExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.PythonExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.PythonExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.PythonExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.PythonExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.PythonExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.PythonExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.PythonExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.PythonExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.PythonExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.PythonExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.PythonExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.PythonExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.PythonExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.PythonExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.PythonExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.PythonExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# RSTExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## Exports reStructuredText documents.

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.RSTExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.RSTExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.RSTExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.RSTExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.RSTExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.RSTExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.RSTExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.RSTExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.RSTExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.RSTExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.RSTExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.RSTExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.RSTExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.RSTExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.RSTExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.RSTExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.RSTExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.RSTExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.RSTExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.RSTExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# ScriptExporter(TemplateExporter) configuration
#------------------------------------------------------------------------------
## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.ScriptExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.ScriptExporter.enabled = True

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.ScriptExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.ScriptExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.ScriptExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.ScriptExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.ScriptExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.ScriptExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.ScriptExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.ScriptExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.ScriptExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.ScriptExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.ScriptExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.ScriptExporter.filters = {}

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.ScriptExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.ScriptExporter.raw_mimetypes = []

#  See also: TemplateExporter.template_extension
# c.ScriptExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.ScriptExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.ScriptExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.ScriptExporter.template_paths = ['.']

#------------------------------------------------------------------------------
# SlidesExporter(HTMLExporter) configuration
#------------------------------------------------------------------------------
## Exports HTML slides with reveal.js

## The text used as the text for anchor links.
#  See also: HTMLExporter.anchor_link_text
# c.SlidesExporter.anchor_link_text = '¶'

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.SlidesExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.SlidesExporter.enabled = True

## If anchor links should be included or not.
#  See also: HTMLExporter.exclude_anchor_links
# c.SlidesExporter.exclude_anchor_links = False

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.SlidesExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.SlidesExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.SlidesExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.SlidesExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.SlidesExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.SlidesExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.SlidesExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.SlidesExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.SlidesExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.SlidesExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.SlidesExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.SlidesExporter.filters = {}

## URL to load font awesome from.
#  
#  Defaults to loading from cdnjs.
#  Default: 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css'
# c.SlidesExporter.font_awesome_url = 'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.css'

## 
#  See also: HTMLExporter.jquery_url
# c.SlidesExporter.jquery_url = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js'

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.SlidesExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.SlidesExporter.raw_mimetypes = []

## 
#  See also: HTMLExporter.require_js_url
# c.SlidesExporter.require_js_url = 'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js'

## If True, enable scrolling within each slide
#  Default: False
# c.SlidesExporter.reveal_scroll = False

## Name of the reveal.js theme to use.
#  
#  We look for a file with this name under
#  ``reveal_url_prefix``/css/theme/``reveal_theme``.css.
#  
#  https://github.com/hakimel/reveal.js/tree/master/css/theme has list of themes
#  that ship by default with reveal.js.
#  Default: 'simple'
# c.SlidesExporter.reveal_theme = 'simple'

## Name of the reveal.js transition to use.
#  
#  The list of transitions that ships by default with reveal.js are: none, fade,
#  slide, convex, concave and zoom.
#  Default: 'slide'
# c.SlidesExporter.reveal_transition = 'slide'

## The URL prefix for reveal.js (version 3.x). This defaults to the reveal CDN,
#  but can be any url pointing to a copy  of reveal.js.
#  
#  For speaker notes to work, this must be a relative path to a local  copy of
#  reveal.js: e.g., "reveal.js".
#  
#  If a relative path is given, it must be a subdirectory of the current
#  directory (from which the server is run).
#  
#  See the usage documentation
#  (https://nbconvert.readthedocs.io/en/latest/usage.html#reveal-js-html-
#  slideshow) for more details.
#  Default: ''
# c.SlidesExporter.reveal_url_prefix = ''

#  See also: TemplateExporter.template_extension
# c.SlidesExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.SlidesExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.SlidesExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.SlidesExporter.template_paths = ['.']

## Template specific theme(e.g. the JupyterLab CSS theme for the lab template)
#  See also: HTMLExporter.theme
# c.SlidesExporter.theme = 'light'

#------------------------------------------------------------------------------
# WebPDFExporter(HTMLExporter) configuration
#------------------------------------------------------------------------------
## Writer designed to write to PDF files.
#  
#  This inherits from :class:`HTMLExporter`. It creates the HTML using the
#  template machinery, and then run pyppeteer to create a pdf.

## Whether to allow downloading Chromium if no suitable version is found on the
#  system.
#  Default: False
# c.WebPDFExporter.allow_chromium_download = False

## The text used as the text for anchor links.
#  See also: HTMLExporter.anchor_link_text
# c.WebPDFExporter.anchor_link_text = '¶'

## List of preprocessors available by default, by name, namespace,
#  See also: Exporter.default_preprocessors
# c.WebPDFExporter.default_preprocessors = ['nbconvert.preprocessors.TagRemovePreprocessor', 'nbconvert.preprocessors.RegexRemovePreprocessor', 'nbconvert.preprocessors.ClearOutputPreprocessor', 'nbconvert.preprocessors.ExecutePreprocessor', 'nbconvert.preprocessors.coalesce_streams', 'nbconvert.preprocessors.SVG2PDFPreprocessor', 'nbconvert.preprocessors.LatexPreprocessor', 'nbconvert.preprocessors.HighlightMagicsPreprocessor', 'nbconvert.preprocessors.ExtractOutputPreprocessor', 'nbconvert.preprocessors.ClearMetadataPreprocessor']

## Disable this exporter (and any exporters inherited from it).
#  See also: Exporter.enabled
# c.WebPDFExporter.enabled = True

## If anchor links should be included or not.
#  See also: HTMLExporter.exclude_anchor_links
# c.WebPDFExporter.exclude_anchor_links = False

## This allows you to exclude code cells from all templates if set to True.
#  See also: TemplateExporter.exclude_code_cell
# c.WebPDFExporter.exclude_code_cell = False

## This allows you to exclude code cell inputs from all templates if set to True.
#  See also: TemplateExporter.exclude_input
# c.WebPDFExporter.exclude_input = False

## This allows you to exclude input prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_input_prompt
# c.WebPDFExporter.exclude_input_prompt = False

## This allows you to exclude markdown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_markdown
# c.WebPDFExporter.exclude_markdown = False

## This allows you to exclude code cell outputs from all templates if set to
#  True.
#  See also: TemplateExporter.exclude_output
# c.WebPDFExporter.exclude_output = False

## This allows you to exclude output prompts from all templates if set to True.
#  See also: TemplateExporter.exclude_output_prompt
# c.WebPDFExporter.exclude_output_prompt = False

## This allows you to exclude raw cells from all templates if set to True.
#  See also: TemplateExporter.exclude_raw
# c.WebPDFExporter.exclude_raw = False

## This allows you to exclude unknown cells from all templates if set to True.
#  See also: TemplateExporter.exclude_unknown
# c.WebPDFExporter.exclude_unknown = False

#  See also: TemplateExporter.extra_template_basedirs
# c.WebPDFExporter.extra_template_basedirs = []

#  See also: TemplateExporter.extra_template_paths
# c.WebPDFExporter.extra_template_paths = []

## Extension of the file that should be written to disk
#  See also: Exporter.file_extension
# c.WebPDFExporter.file_extension = ''

## Dictionary of filters, by name and namespace, to add to the Jinja
#  See also: TemplateExporter.filters
# c.WebPDFExporter.filters = {}

## 
#  See also: HTMLExporter.jquery_url
# c.WebPDFExporter.jquery_url = 'https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js'

## List of preprocessors, by name or namespace, to enable.
#  See also: Exporter.preprocessors
# c.WebPDFExporter.preprocessors = []

## formats of raw cells to be included in this Exporter's output.
#  See also: TemplateExporter.raw_mimetypes
# c.WebPDFExporter.raw_mimetypes = []

## 
#  See also: HTMLExporter.require_js_url
# c.WebPDFExporter.require_js_url = 'https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js'

#  See also: TemplateExporter.template_extension
# c.WebPDFExporter.template_extension = ''

## Name of the template file to use
#  See also: TemplateExporter.template_file
# c.WebPDFExporter.template_file = None

## Name of the template to use
#  See also: TemplateExporter.template_name
# c.WebPDFExporter.template_name = ''

#  See also: TemplateExporter.template_paths
# c.WebPDFExporter.template_paths = ['.']

## Template specific theme(e.g. the JupyterLab CSS theme for the lab template)
#  See also: HTMLExporter.theme
# c.WebPDFExporter.theme = 'light'

#------------------------------------------------------------------------------
# Preprocessor(NbConvertBase) configuration
#------------------------------------------------------------------------------
## A configurable preprocessor
#  
#  Inherit from this class if you wish to have configurability for your
#  preprocessor.
#  
#  Any configurable traitlets this class exposed will be configurable in profiles
#  using c.SubClassName.attribute = value
#  
#  You can overwrite `preprocess_cell()` to apply a transformation independently
#  on each cell or `preprocess()` if you prefer your own logic. See corresponding
#  docstring for information.
#  
#  Disabled by default and can be enabled via the config by
#      'c.YourPreprocessorName.enabled = True'

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.Preprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.Preprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  Default: False
# c.Preprocessor.enabled = False

#------------------------------------------------------------------------------
# CSSHTMLHeaderPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor used to pre-process notebook for HTML output.  Adds IPython
#  notebook front-end CSS and Pygments CSS to HTML output.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.CSSHTMLHeaderPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.CSSHTMLHeaderPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.CSSHTMLHeaderPreprocessor.enabled = False

## CSS highlight class identifier
#  Default: '.highlight'
# c.CSSHTMLHeaderPreprocessor.highlight_class = '.highlight'

## Name of the pygments style to use
#  Default: <class 'jupyterlab_pygments.style.JupyterStyle'>
# c.CSSHTMLHeaderPreprocessor.style = <class 'jupyterlab_pygments.style.JupyterStyle'>

#------------------------------------------------------------------------------
# ClearMetadataPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Removes all the metadata from all code cells in a notebook.

## Flag to choose if cell metadata is to be cleared in addition to notebook
#  metadata.
#  Default: True
# c.ClearMetadataPreprocessor.clear_cell_metadata = True

## Flag to choose if notebook metadata is to be cleared in addition to cell
#  metadata.
#  Default: True
# c.ClearMetadataPreprocessor.clear_notebook_metadata = True

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ClearMetadataPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ClearMetadataPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ClearMetadataPreprocessor.enabled = False

## Indicates the key paths to preserve when deleting metadata across both cells
#  and notebook metadata fields. Tuples of keys can be passed to preserved
#  specific nested values
#  Default: set()
# c.ClearMetadataPreprocessor.preserve_cell_metadata_mask = set()

## Indicates the key paths to preserve when deleting metadata across both cells
#  and notebook metadata fields. Tuples of keys can be passed to preserved
#  specific nested values
#  Default: {('language_info', 'name')}
# c.ClearMetadataPreprocessor.preserve_nb_metadata_mask = {('language_info', 'name')}

#------------------------------------------------------------------------------
# ClearOutputPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Removes the output from all code cells in a notebook.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ClearOutputPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ClearOutputPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ClearOutputPreprocessor.enabled = False

#  Default: {'collapsed', 'scrolled'}
# c.ClearOutputPreprocessor.remove_metadata_fields = {'collapsed', 'scrolled'}

#------------------------------------------------------------------------------
# ConvertFiguresPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Converts all of the outputs in a notebook from one format to another.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ConvertFiguresPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ConvertFiguresPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ConvertFiguresPreprocessor.enabled = False

## Format the converter accepts
#  Default: ''
# c.ConvertFiguresPreprocessor.from_format = ''

## Format the converter writes
#  Default: ''
# c.ConvertFiguresPreprocessor.to_format = ''

#------------------------------------------------------------------------------
# NotebookClient(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Encompasses a Client for executing cells in a notebook

## If ``False`` (default), when a cell raises an error the execution is stopped
#  and a `CellExecutionError` is raised. If ``True``, execution errors are
#  ignored and the execution is continued until the end of the notebook. Output
#  from exceptions is included in the cell output in both cases.
#  Default: False
c.NotebookClient.allow_errors = True

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']
# c.NotebookClient.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  Default: []
# c.NotebookClient.extra_arguments = []

## If False (default), errors from executing the notebook can be allowed with a
#  ``raises-exception`` tag on a single cell, or the ``allow_errors``
#  configurable option for all cells. An allowed error will be recorded in
#  notebook output, and execution will continue. If an error occurs when it is
#  not explicitly allowed, a `CellExecutionError` will be raised. If True,
#  `CellExecutionError` will be raised for any error that occurs while executing
#  the notebook. This overrides both the ``allow_errors`` option and the
#  ``raises-exception`` cell tag.
#  Default: False
# c.NotebookClient.force_raise_errors = False

## If execution of a cell times out, interrupt the kernel and continue executing
#  other cells rather than throwing an error and stopping.
#  Default: False
# c.NotebookClient.interrupt_on_timeout = False

## The time to wait (in seconds) for IOPub output. This generally doesn't need to
#  be set, but on some slow networks (such as CI systems) the default timeout
#  might not be long enough to get all messages.
#  Default: 4
# c.NotebookClient.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  
#  The specific value ``:memory:`` (including the colon at both end but not the
#  back ticks), avoids creating a history file. Otherwise, IPython will create a
#  history file for each kernel.
#  
#  When running kernels simultaneously (e.g. via multiprocessing) saving history
#  a single SQLite file can result in database errors, so using ``:memory:`` is
#  recommended in non-interactive contexts.
#  Default: ':memory:'
# c.NotebookClient.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  Default: 'builtins.object'
# c.NotebookClient.kernel_manager_class = 'builtins.object'

## Name of kernel to use to execute the cells. If not set, use the kernel_spec
#  embedded in the notebook.
#  Default: ''
# c.NotebookClient.kernel_name = ''

## If ``False`` (default), then the kernel will continue waiting for iopub
#  messages until it receives a kernel idle message, or until a timeout occurs,
#  at which point the currently executing cell will be skipped. If ``True``, then
#  an error will be raised after the first timeout. This option generally does
#  not need to be used, but may be useful in contexts where there is the
#  possibility of executing notebooks with memory-consuming infinite loops.
#  Default: False
# c.NotebookClient.raise_on_iopub_timeout = False

## If ``True`` (default), then the execution timings of each cell will be stored
#  in the metadata of the notebook.
#  Default: True
# c.NotebookClient.record_timing = True

## The time to wait (in seconds) for Shell output before retrying. This generally
#  doesn't need to be set, but if one needs to check for dead kernels at a faster
#  rate this can help.
#  Default: 5
# c.NotebookClient.shell_timeout_interval = 5

## If ``graceful`` (default), then the kernel is given time to clean up after
#  executing all cells, e.g., to execute its ``atexit`` hooks. If ``immediate``,
#  then the kernel is signaled to immediately terminate.
#  Choices: any of ['graceful', 'immediate']
#  Default: 'graceful'
# c.NotebookClient.shutdown_kernel = 'graceful'

## The time to wait (in seconds) for the kernel to start. If kernel startup takes
#  longer, a RuntimeError is raised.
#  Default: 60
# c.NotebookClient.startup_timeout = 60

## If ``True`` (default), then the state of the Jupyter widgets created at the
#  kernel will be stored in the metadata of the notebook.
#  Default: True
# c.NotebookClient.store_widget_state = True

## The time to wait (in seconds) for output from executions. If a cell execution
#  takes longer, a TimeoutError is raised.
#  
#  ``None`` or ``-1`` will disable the timeout. If ``timeout_func`` is set, it
#  overrides ``timeout``.
#  Default: None
# c.NotebookClient.timeout = None

## A callable which, when given the cell source as input, returns the time to
#  wait (in seconds) for output from cell executions. If a cell execution takes
#  longer, a TimeoutError is raised.
#  
#  Returning ``None`` or ``-1`` will disable the timeout for the cell. Not
#  setting ``timeout_func`` will cause the client to default to using the
#  ``timeout`` trait for all cells. The ``timeout_func`` trait overrides
#  ``timeout`` if it is not ``None``.
#  Default: None
# c.NotebookClient.timeout_func = None

#------------------------------------------------------------------------------
# ExecutePreprocessor(Preprocessor, NotebookClient) configuration
#------------------------------------------------------------------------------
## Executes all the cells in a notebook

## 
#  See also: NotebookClient.allow_errors
c.ExecutePreprocessor.allow_errors = True

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ExecutePreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ExecutePreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ExecutePreprocessor.enabled = True

#  See also: NotebookClient.extra_arguments
# c.ExecutePreprocessor.extra_arguments = ['--debug']

## 
#  See also: NotebookClient.force_raise_errors
# c.ExecutePreprocessor.force_raise_errors = False

## 
#  See also: NotebookClient.interrupt_on_timeout
# c.ExecutePreprocessor.interrupt_on_timeout = False

## 
#  See also: NotebookClient.iopub_timeout
# c.ExecutePreprocessor.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  See also: NotebookClient.ipython_hist_file
# c.ExecutePreprocessor.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  See also: NotebookClient.kernel_manager_class
# c.ExecutePreprocessor.kernel_manager_class = 'builtins.object'

## 
#  See also: NotebookClient.kernel_name
# c.ExecutePreprocessor.kernel_name = ''

## 
#  See also: NotebookClient.raise_on_iopub_timeout
# c.ExecutePreprocessor.raise_on_iopub_timeout = False

## 
#  See also: NotebookClient.record_timing
# c.ExecutePreprocessor.record_timing = True

## 
#  See also: NotebookClient.shell_timeout_interval
# c.ExecutePreprocessor.shell_timeout_interval = 5

## 
#  See also: NotebookClient.shutdown_kernel
# c.ExecutePreprocessor.shutdown_kernel = 'graceful'

## 
#  See also: NotebookClient.startup_timeout
# c.ExecutePreprocessor.startup_timeout = 60

## 
#  See also: NotebookClient.store_widget_state
# c.ExecutePreprocessor.store_widget_state = True

## 
#  See also: NotebookClient.timeout
# c.ExecutePreprocessor.timeout = None

## 
#  See also: NotebookClient.timeout_func
# c.ExecutePreprocessor.timeout_func = None

#------------------------------------------------------------------------------
# ExtractOutputPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Extracts all of the outputs from the notebook file.  The extracted outputs are
#  returned in the 'resources' dictionary.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ExtractOutputPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ExtractOutputPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ExtractOutputPreprocessor.enabled = False

#  Default: {'application/pdf', 'image/jpeg', 'image/png', 'image/svg+xml'}
# c.ExtractOutputPreprocessor.extract_output_types = {'application/pdf', 'image/jpeg', 'image/png', 'image/svg+xml'}

#  Default: '{unique_key}_{cell_index}_{index}{extension}'
# c.ExtractOutputPreprocessor.output_filename_template = '{unique_key}_{cell_index}_{index}{extension}'

#------------------------------------------------------------------------------
# HighlightMagicsPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Detects and tags code cells that use a different languages than Python.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.HighlightMagicsPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.HighlightMagicsPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.HighlightMagicsPreprocessor.enabled = False

## Syntax highlighting for magic's extension languages. Each item associates a
#  language magic extension such as %%R, with a pygments lexer such as r.
#  Default: {}
# c.HighlightMagicsPreprocessor.languages = {}

#------------------------------------------------------------------------------
# LatexPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor for latex destined documents.
#  
#  Mainly populates the ``latex`` key in the resources dict, adding definitions
#  for pygments highlight styles.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.LatexPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.LatexPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.LatexPreprocessor.enabled = False

## Name of the pygments style to use
#  Default: 'default'
# c.LatexPreprocessor.style = 'default'

#------------------------------------------------------------------------------
# RegexRemovePreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Removes cells from a notebook that match one or more regular expression.
#  
#  For each cell, the preprocessor checks whether its contents match the regular
#  expressions in the ``patterns`` traitlet which is a list of unicode strings.
#  If the contents match any of the patterns, the cell is removed from the
#  notebook.
#  
#  To modify the list of matched patterns, modify the patterns traitlet. For
#  example, execute the following command to convert a notebook to html and
#  remove cells containing only whitespace::
#  
#    jupyter nbconvert --RegexRemovePreprocessor.patterns="['\s*\Z']"
#  mynotebook.ipynb
#  
#  The command line argument sets the list of patterns to ``'\s*\Z'`` which
#  matches an arbitrary number of whitespace characters followed by the end of
#  the string.
#  
#  See https://regex101.com/ for an interactive guide to regular expressions
#  (make sure to select the python flavor). See
#  https://docs.python.org/library/re.html for the official regular expression
#  documentation in python.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.RegexRemovePreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.RegexRemovePreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.RegexRemovePreprocessor.enabled = False

#  Default: []
# c.RegexRemovePreprocessor.patterns = []

#------------------------------------------------------------------------------
# SVG2PDFPreprocessor(ConvertFiguresPreprocessor) configuration
#------------------------------------------------------------------------------
## Converts all of the outputs in a notebook from SVG to PDF.

## The command to use for converting SVG to PDF
#  
#  This string is a template, which will be formatted with the keys to_filename
#  and from_filename.
#  
#  The conversion call must read the SVG from {from_filename}, and write a PDF to
#  {to_filename}.
#  Default: ''
# c.SVG2PDFPreprocessor.command = ''

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.SVG2PDFPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.SVG2PDFPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.SVG2PDFPreprocessor.enabled = False

## Format the converter accepts
#  See also: ConvertFiguresPreprocessor.from_format
# c.SVG2PDFPreprocessor.from_format = ''

## The path to Inkscape, if necessary
#  Default: ''
# c.SVG2PDFPreprocessor.inkscape = ''

## The version of inkscape being used.
#  
#  This affects how the conversion command is run.
#  Default: ''
# c.SVG2PDFPreprocessor.inkscape_version = ''

## Format the converter writes
#  See also: ConvertFiguresPreprocessor.to_format
# c.SVG2PDFPreprocessor.to_format = ''

#------------------------------------------------------------------------------
# TagRemovePreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Removes inputs, outputs, or cells from a notebook that have tags that
#  designate they are to be removed prior to exporting the notebook.
#  
#  remove_cell_tags
#      removes cells tagged with these values
#  
#  remove_all_outputs_tags
#      removes entire output areas on cells
#      tagged with these values
#  
#  remove_single_output_tags
#      removes individual output objects on
#      outputs tagged with these values
#  
#  remove_input_tags
#      removes inputs tagged with these values

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.TagRemovePreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.TagRemovePreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.TagRemovePreprocessor.enabled = False

## Tags indicating cells for which the outputs are to be removed,matches tags in
#  ``cell.metadata.tags``.
#  Default: set()
# c.TagRemovePreprocessor.remove_all_outputs_tags = set()

## Tags indicating which cells are to be removed,matches tags in
#  ``cell.metadata.tags``.
#  Default: set()
# c.TagRemovePreprocessor.remove_cell_tags = set()

## Tags indicating cells for which input is to be removed,matches tags in
#  ``cell.metadata.tags``.
#  Default: set()
# c.TagRemovePreprocessor.remove_input_tags = set()

#  Default: {'collapsed', 'scrolled'}
# c.TagRemovePreprocessor.remove_metadata_fields = {'collapsed', 'scrolled'}

## Tags indicating which individual outputs are to be removed,matches output *i*
#  tags in ``cell.outputs[i].metadata.tags``.
#  Default: set()
# c.TagRemovePreprocessor.remove_single_output_tags = set()

#------------------------------------------------------------------------------
# WriterBase(NbConvertBase) configuration
#------------------------------------------------------------------------------
## Consumes output from nbconvert export...() methods and writes to a useful
#  location.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.WriterBase.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.WriterBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## List of the files that the notebook references.  Files will be  included with
#  written output.
#  Default: []
# c.WriterBase.files = []

#------------------------------------------------------------------------------
# DebugWriter(WriterBase) configuration
#------------------------------------------------------------------------------
## Consumes output from nbconvert export...() methods and writes useful debugging
#  information to the stdout.  The information includes a list of resources that
#  were extracted from the notebook(s) during export.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.DebugWriter.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.DebugWriter.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## 
#  See also: WriterBase.files
# c.DebugWriter.files = []

#------------------------------------------------------------------------------
# FilesWriter(WriterBase) configuration
#------------------------------------------------------------------------------
## Consumes nbconvert output and produces files.

## Directory to write output(s) to. Defaults to output to the directory of each
#  notebook. To recover previous default behaviour (outputting to the current
#  working directory) use . as the flag value.
#  Default: ''
# c.FilesWriter.build_directory = ''

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.FilesWriter.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.FilesWriter.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## 
#  See also: WriterBase.files
# c.FilesWriter.files = []

## When copying files that the notebook depends on, copy them in relation to this
#  path, such that the destination filename will be os.path.relpath(filename,
#  relpath). If FilesWriter is operating on a notebook that already exists
#  elsewhere on disk, then the default will be the directory containing that
#  notebook.
#  Default: ''
# c.FilesWriter.relpath = ''

#------------------------------------------------------------------------------
# StdoutWriter(WriterBase) configuration
#------------------------------------------------------------------------------
## Consumes output from nbconvert export...() methods and writes to the  stdout
#  stream.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.StdoutWriter.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.StdoutWriter.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## 
#  See also: WriterBase.files
# c.StdoutWriter.files = []

#------------------------------------------------------------------------------
# PostProcessorBase(NbConvertBase) configuration
#------------------------------------------------------------------------------
## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.PostProcessorBase.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.PostProcessorBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#------------------------------------------------------------------------------
# ServePostProcessor(PostProcessorBase) configuration
#------------------------------------------------------------------------------
## Post processor designed to serve files
#  
#  Proxies reveal.js requests to a CDN if no local reveal.js is present

## Specify what browser should be used to open slides. See
#  https://docs.python.org/3/library/webbrowser.html#webbrowser.register to see
#  how keys are mapped to browser executables. If  not specified, the default
#  browser will be determined  by the `webbrowser`  standard library module,
#  which allows setting of the BROWSER  environment variable to override it.
#  Default: ''
# c.ServePostProcessor.browser = ''

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ServePostProcessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ServePostProcessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## The IP address to listen on.
#  Default: '127.0.0.1'
# c.ServePostProcessor.ip = '127.0.0.1'

## Should the browser be opened automatically?
#  Default: True
# c.ServePostProcessor.open_in_browser = True

## port for the server to listen on.
#  Default: 8000
# c.ServePostProcessor.port = 8000

## URL for reveal.js CDN.
#  Default: 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0'
# c.ServePostProcessor.reveal_cdn = 'https://cdnjs.cloudflare.com/ajax/libs/reveal.js/3.5.0'

## URL prefix for reveal.js
#  Default: 'reveal.js'
# c.ServePostProcessor.reveal_prefix = 'reveal.js'

