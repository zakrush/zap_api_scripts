from scan_core import context, colors, sessionManagement
from scan_core.shared_core import get_context_id_by_name


def set_contex_properties(contextname='Default Context', include_url=None, exclude_url=None, technology=None,
                          session_management='cookieBasedSessionManagement'):
    """Setup context. This function return context_id. If contextname is not set, it was set for Default Context"""
    if contextname == 'Default Context':
        context_id = get_context_id_by_name(contextname)
    else:
        context.remove_context(contextname=contextname)
        context_id = context.new_context(contextname=contextname)
    print(colors.Bcolors.CN + 'Set Context properties')
    # Add urls into context
    if include_url is not None:
        [print('Included into context URL: ' + url + ' -> ' + context.include_in_context(contextname=contextname,
                                                                                         regex=url))
         for url in include_url]

    # Exclude urls from context
    if exclude_url is not None:
        [print('Excluded from context URL: ' + url + '->' + context.exclude_from_context(contextname=contextname,
                                                                                         regex=url))
         for url in exclude_url]

    # Set technology list
    if technology is not None:
        context.exclude_all_context_technologies(contextname=contextname)
        print(colors.Bcolors.Y + ' Set context technology list: ' + colors.Bcolors.CL + ' ' +
              context.include_context_technologies(contextname=contextname, technologynames=', '.join(technology)))
        # Setup session management for the context.
    # There is no methodconfigparams to provide for both current methods
    print(
        colors.Bcolors.Y + ' Set session management method: ' + colors.Bcolors.CL + ' ' + session_management + ' -> ' +
        sessionManagement.set_session_management_method(
            contextid=context_id, methodname=session_management,
            methodconfigparams=None))
    return context_id


def remove_default_context():
    return context.remove_context('Default Context')
