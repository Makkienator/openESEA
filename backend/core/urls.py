from django.urls import path, include
from rest_framework_nested import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from .views import (membershipview, respondentview, userview, networkview, network_memberview, organisationview, organisation_memberview, methodview, surveyview, sectionview, questionview, text_fragmentview, 
                    topicview, direct_indicatorview2, indirect_indicatorview, survey_responseview, campaignview, esea_accountview, reportview)
 

router = routers.DefaultRouter()
router.register(r'memberships', membershipview.MembershipViewSet, basename="Memberships")
router.register(r'respondents', respondentview.RespondentsViewSet, basename="Respondents")
router.register(r'users', userview.UsersViewSet, basename="Users")
router.register(r'networks', networkview.NetworkViewSet, basename="Networks")
router.register(r'organisations', organisationview.OrganisationViewSet, basename="Organisations")
router.register(r'methods', methodview.MethodViewSet, basename='methods')   ## /methods/ & /methods/{pk}/

network_router = routers.NestedSimpleRouter(router, r'networks', lookup="network")
network_router.register(r'campaigns', campaignview.CampaignViewSet, basename="network-campaigns" )
network_router.register(r'members', network_memberview.NetworkMemberViewSet, basename="network-members")

organisation_router = routers.NestedSimpleRouter(router, r'organisations', lookup="organisation")
organisation_router.register(r'esea-accounts', esea_accountview.EseaAccountViewSet, basename="organisation-esea-accounts")
organisation_router.register(r'members', organisation_memberview.OrganisationMemberViewSet, basename="organisation-members")

esea_account_router = routers.NestedSimpleRouter(organisation_router, r'esea-accounts', lookup="esea_account")
# esea_account_router.register(r'surveys', surveyview.SurveyViewSet, basename="esea-account-surveys")

# esea_account_survey_router = routers.NestedSimpleRouter(esea_account_router, r'surveys', lookup="survey")
esea_account_router.register(r'responses', survey_responseview.SurveyResponseViewSet, basename='responses')

method_router = routers.NestedSimpleRouter(router, r'methods', lookup="method")
method_router.register(r'surveys', surveyview.SurveyViewSet, basename="method-surveys")

method_router.register(r'topics', topicview.TopicViewSet, basename="method-topics") 
method_router.register(r'direct-indicators', direct_indicatorview2.DirectIndicatorViewSet, basename="method-direct-indicators")
method_router.register(r'indirect-indicators', indirect_indicatorview.IndirectIndicatorViewSet, basename="method-indirect-indicators")
# 

survey_router = routers.NestedSimpleRouter(method_router, r'surveys', lookup="survey")
survey_router.register(r'sections', sectionview.SectionViewSet, basename="survey-sections")
survey_router.register(r'organisations', organisationview.OrganisationViewSet, basename="survey-organisations")

section_router = routers.NestedSimpleRouter(survey_router, r'sections', lookup="section")
section_router.register(r'questions', questionview.QuestionViewSet, basename="section-questions")
section_router.register(r'text-fragments', text_fragmentview.TextFragmentViewSet, basename="section-text-fragments")


urlpatterns = [
    path('account/register/', userview.RegisterUserView.as_view(), name='user_registration'),
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-refresh/', TokenRefreshView.as_view()),
    path('import-method/', methodview.upload_method),
    path('import-employees/<int:eseaaccount_pk>/<int:survey_pk>/', esea_accountview.import_employees, name="import_employees_of_organisation"),
    path('audit-account/<int:eseaaccount_pk>/', reportview.audit_eseaaccount, name="audit_esea_account"),
    path('', include(router.urls)),
    path('', include(network_router.urls)),
    path('', include(method_router.urls)),
    path('', include(survey_router.urls)),
    path('', include(esea_account_router.urls)),
    path('', include(section_router.urls)),
    path('', include(organisation_router.urls)),
]



''' TODO
- method_router.register(r'certification-levels', certification_levelview.CertificationLevelViewSet, basename="method-certification-levels")
'''