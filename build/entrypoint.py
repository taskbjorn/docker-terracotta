'''Entrypoint module for the docker-terracotta container
'''

import subprocess


def main():
    """Entrypoint main method.
    """
    # Build the documentation.
    subprocess.call(
        'terracotta optimize-rasters --output-folder /terracotta/optimized --overwrite /terracotta/rasters/*.tif')

    #
    subprocess.call(
        'terracotta ingest --output-file terracotta.sqlite /terracotta/optimized/{name}.tif')

    # Launch the Terracotta XYZ tile server.
    subprocess.call(
        'terracotta serve --database /terracotta/terracotta.sqlite --port 5100 --allow-all-ips')


if __name__ == '__main__':
    main()
