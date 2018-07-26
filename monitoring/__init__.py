# coding: utf-8
__author__ = 'Alison Mukoma <alison@kartoza.com>'
__copyright__ = 'kartoza.com'

# custom monitoring scripts
from prometheus_client import Counter

landing_page_counter = Counter(
                'open_landing_page',
                'User open the landing page')


class PrometheusCounter:

    @staticmethod
    def increase_landing_page_view():
        landing_page_counter.inc()

