# kolibri-content-tools
Shared functionality for working with Kolibri content files and databases.

#### Contents

`kolibri_content`

This module contains a backwards-compatible Django
representation of the Kolibri data structures. It is
used by `ricecooker` and `Studio` for publishing
Kolibri databases.

`kolibri_content_tools/kolibri_db`

Tools for working with Kolibri db files, including
reading and writing.

`kolibri_content_tools/search`

Tools for indexing and searching the various content
formats that Kolibri can handle. Uses whoosh to provide
offline-friendly pure-Python indexing and search
capabilities.
