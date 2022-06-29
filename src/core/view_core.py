from rest_framework.request import Request


class ViewCore:
    def initialize_request(self, request, *args, **kwargs):
        request.property_name = self.__class__.__name__

        parser_context = self.get_parser_context(request)

        return Request(
            request,
            parsers=self.get_parsers(),
            authenticators=self.get_authenticators(),
            negotiator=self.get_content_negotiator(),
            parser_context=parser_context
        )
