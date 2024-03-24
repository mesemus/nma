from invenio_records_resources.services import SearchOptions as InvenioSearchOptions

from . import facets


class DatasetsSearchOptions(InvenioSearchOptions):
    """DatasetsRecord search options."""

    facet_groups = {}

    facets = {
        "metadata_alternateIdentifiers_alternateIdentifier": facets.metadata_alternateIdentifiers_alternateIdentifier,
        "metadata_alternateIdentifiers_alternateIdentifierType": facets.metadata_alternateIdentifiers_alternateIdentifierType,
        "metadata_container_firstPage": facets.metadata_container_firstPage,
        "metadata_container_title": facets.metadata_container_title,
        "metadata_container_type": facets.metadata_container_type,
        "metadata_contributors_affiliation_affiliationIdentifier": facets.metadata_contributors_affiliation_affiliationIdentifier,
        "metadata_contributors_affiliation_affiliationIdentifierScheme": facets.metadata_contributors_affiliation_affiliationIdentifierScheme,
        "metadata_contributors_affiliation_name": facets.metadata_contributors_affiliation_name,
        "metadata_contributors_affiliation_schemeURI": facets.metadata_contributors_affiliation_schemeURI,
        "metadata_contributors_contributorType": facets.metadata_contributors_contributorType,
        "metadata_contributors_familyName": facets.metadata_contributors_familyName,
        "metadata_contributors_givenName": facets.metadata_contributors_givenName,
        "metadata_contributors_lang": facets.metadata_contributors_lang,
        "metadata_contributors_name": facets.metadata_contributors_name,
        "metadata_contributors_nameIdentifiers_nameIdentifier": facets.metadata_contributors_nameIdentifiers_nameIdentifier,
        "metadata_contributors_nameIdentifiers_nameIdentifierScheme": facets.metadata_contributors_nameIdentifiers_nameIdentifierScheme,
        "metadata_contributors_nameIdentifiers_schemeURI": facets.metadata_contributors_nameIdentifiers_schemeURI,
        "metadata_contributors_nameType": facets.metadata_contributors_nameType,
        "metadata_creators_affiliation_affiliationIdentifier": facets.metadata_creators_affiliation_affiliationIdentifier,
        "metadata_creators_affiliation_affiliationIdentifierScheme": facets.metadata_creators_affiliation_affiliationIdentifierScheme,
        "metadata_creators_affiliation_name": facets.metadata_creators_affiliation_name,
        "metadata_creators_affiliation_schemeURI": facets.metadata_creators_affiliation_schemeURI,
        "metadata_creators_familyName": facets.metadata_creators_familyName,
        "metadata_creators_givenName": facets.metadata_creators_givenName,
        "metadata_creators_lang": facets.metadata_creators_lang,
        "metadata_creators_name": facets.metadata_creators_name,
        "metadata_creators_nameIdentifiers_nameIdentifier": facets.metadata_creators_nameIdentifiers_nameIdentifier,
        "metadata_creators_nameIdentifiers_nameIdentifierScheme": facets.metadata_creators_nameIdentifiers_nameIdentifierScheme,
        "metadata_creators_nameIdentifiers_schemeURI": facets.metadata_creators_nameIdentifiers_schemeURI,
        "metadata_creators_nameType": facets.metadata_creators_nameType,
        "metadata_dates_date": facets.metadata_dates_date,
        "metadata_dates_dateInformation": facets.metadata_dates_dateInformation,
        "metadata_dates_dateType": facets.metadata_dates_dateType,
        "metadata_descriptions_descriptionType": facets.metadata_descriptions_descriptionType,
        "metadata_descriptions_lang": facets.metadata_descriptions_lang,
        "metadata_doi": facets.metadata_doi,
        "metadata_formats": facets.metadata_formats,
        "metadata_fundingReferences_awardNumber": facets.metadata_fundingReferences_awardNumber,
        "metadata_fundingReferences_awardTitle": facets.metadata_fundingReferences_awardTitle,
        "metadata_fundingReferences_awardURI": facets.metadata_fundingReferences_awardURI,
        "metadata_fundingReferences_funderIdentifier": facets.metadata_fundingReferences_funderIdentifier,
        "metadata_fundingReferences_funderIdentifierType": facets.metadata_fundingReferences_funderIdentifierType,
        "metadata_fundingReferences_funderName": facets.metadata_fundingReferences_funderName,
        "metadata_geoLocations_geoLocationBox_eastBoundLongitude": facets.metadata_geoLocations_geoLocationBox_eastBoundLongitude,
        "metadata_geoLocations_geoLocationBox_northBoundLatitude": facets.metadata_geoLocations_geoLocationBox_northBoundLatitude,
        "metadata_geoLocations_geoLocationBox_southBoundLatitude": facets.metadata_geoLocations_geoLocationBox_southBoundLatitude,
        "metadata_geoLocations_geoLocationBox_westBoundLongitude": facets.metadata_geoLocations_geoLocationBox_westBoundLongitude,
        "metadata_geoLocations_geoLocationPlace": facets.metadata_geoLocations_geoLocationPlace,
        "metadata_geoLocations_geoLocationPoint_pointLatitude": facets.metadata_geoLocations_geoLocationPoint_pointLatitude,
        "metadata_geoLocations_geoLocationPoint_pointLongitude": facets.metadata_geoLocations_geoLocationPoint_pointLongitude,
        "metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLatitude": facets.metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLatitude,
        "metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLongitude": facets.metadata_geoLocations_geoLocationPolygons_inPolygonPoint_pointLongitude,
        "metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLatitude": facets.metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLatitude,
        "metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLongitude": facets.metadata_geoLocations_geoLocationPolygons_polygonPoints_pointLongitude,
        "metadata_language": facets.metadata_language,
        "metadata_publicationYear": facets.metadata_publicationYear,
        "metadata_publisher_lang": facets.metadata_publisher_lang,
        "metadata_publisher_name": facets.metadata_publisher_name,
        "metadata_publisher_publisherIdentifier": facets.metadata_publisher_publisherIdentifier,
        "metadata_publisher_publisherIdentifierScheme": facets.metadata_publisher_publisherIdentifierScheme,
        "metadata_publisher_schemeURI": facets.metadata_publisher_schemeURI,
        "metadata_relatedIdentifiers_relatedIdentifier": facets.metadata_relatedIdentifiers_relatedIdentifier,
        "metadata_relatedIdentifiers_relatedIdentifierType": facets.metadata_relatedIdentifiers_relatedIdentifierType,
        "metadata_relatedIdentifiers_relatedMetadataScheme": facets.metadata_relatedIdentifiers_relatedMetadataScheme,
        "metadata_relatedIdentifiers_relationType": facets.metadata_relatedIdentifiers_relationType,
        "metadata_relatedIdentifiers_resourceTypeGeneral": facets.metadata_relatedIdentifiers_resourceTypeGeneral,
        "metadata_relatedIdentifiers_schemeType": facets.metadata_relatedIdentifiers_schemeType,
        "metadata_relatedIdentifiers_schemeURI": facets.metadata_relatedIdentifiers_schemeURI,
        "metadata_relatedItems_contributors_affiliation_affiliationIdentifier": facets.metadata_relatedItems_contributors_affiliation_affiliationIdentifier,
        "metadata_relatedItems_contributors_affiliation_affiliationIdentifierScheme": facets.metadata_relatedItems_contributors_affiliation_affiliationIdentifierScheme,
        "metadata_relatedItems_contributors_affiliation_name": facets.metadata_relatedItems_contributors_affiliation_name,
        "metadata_relatedItems_contributors_affiliation_schemeURI": facets.metadata_relatedItems_contributors_affiliation_schemeURI,
        "metadata_relatedItems_contributors_contributorType": facets.metadata_relatedItems_contributors_contributorType,
        "metadata_relatedItems_contributors_familyName": facets.metadata_relatedItems_contributors_familyName,
        "metadata_relatedItems_contributors_givenName": facets.metadata_relatedItems_contributors_givenName,
        "metadata_relatedItems_contributors_lang": facets.metadata_relatedItems_contributors_lang,
        "metadata_relatedItems_contributors_name": facets.metadata_relatedItems_contributors_name,
        "metadata_relatedItems_contributors_nameIdentifiers_nameIdentifier": facets.metadata_relatedItems_contributors_nameIdentifiers_nameIdentifier,
        "metadata_relatedItems_contributors_nameIdentifiers_nameIdentifierScheme": facets.metadata_relatedItems_contributors_nameIdentifiers_nameIdentifierScheme,
        "metadata_relatedItems_contributors_nameIdentifiers_schemeURI": facets.metadata_relatedItems_contributors_nameIdentifiers_schemeURI,
        "metadata_relatedItems_contributors_nameType": facets.metadata_relatedItems_contributors_nameType,
        "metadata_relatedItems_creators_affiliation_affiliationIdentifier": facets.metadata_relatedItems_creators_affiliation_affiliationIdentifier,
        "metadata_relatedItems_creators_affiliation_affiliationIdentifierScheme": facets.metadata_relatedItems_creators_affiliation_affiliationIdentifierScheme,
        "metadata_relatedItems_creators_affiliation_name": facets.metadata_relatedItems_creators_affiliation_name,
        "metadata_relatedItems_creators_affiliation_schemeURI": facets.metadata_relatedItems_creators_affiliation_schemeURI,
        "metadata_relatedItems_creators_familyName": facets.metadata_relatedItems_creators_familyName,
        "metadata_relatedItems_creators_givenName": facets.metadata_relatedItems_creators_givenName,
        "metadata_relatedItems_creators_lang": facets.metadata_relatedItems_creators_lang,
        "metadata_relatedItems_creators_name": facets.metadata_relatedItems_creators_name,
        "metadata_relatedItems_creators_nameIdentifiers_nameIdentifier": facets.metadata_relatedItems_creators_nameIdentifiers_nameIdentifier,
        "metadata_relatedItems_creators_nameIdentifiers_nameIdentifierScheme": facets.metadata_relatedItems_creators_nameIdentifiers_nameIdentifierScheme,
        "metadata_relatedItems_creators_nameIdentifiers_schemeURI": facets.metadata_relatedItems_creators_nameIdentifiers_schemeURI,
        "metadata_relatedItems_creators_nameType": facets.metadata_relatedItems_creators_nameType,
        "metadata_relatedItems_edition": facets.metadata_relatedItems_edition,
        "metadata_relatedItems_firstPage": facets.metadata_relatedItems_firstPage,
        "metadata_relatedItems_issue": facets.metadata_relatedItems_issue,
        "metadata_relatedItems_lastPage": facets.metadata_relatedItems_lastPage,
        "metadata_relatedItems_number": facets.metadata_relatedItems_number,
        "metadata_relatedItems_numberType": facets.metadata_relatedItems_numberType,
        "metadata_relatedItems_publicationYear": facets.metadata_relatedItems_publicationYear,
        "metadata_relatedItems_publisher": facets.metadata_relatedItems_publisher,
        "metadata_relatedItems_relatedItemIdentifier_relatedItemIdentifier": facets.metadata_relatedItems_relatedItemIdentifier_relatedItemIdentifier,
        "metadata_relatedItems_relatedItemIdentifier_relatedItemIdentifierType": facets.metadata_relatedItems_relatedItemIdentifier_relatedItemIdentifierType,
        "metadata_relatedItems_relatedItemType": facets.metadata_relatedItems_relatedItemType,
        "metadata_relatedItems_relatedMetadataScheme": facets.metadata_relatedItems_relatedMetadataScheme,
        "metadata_relatedItems_relationType": facets.metadata_relatedItems_relationType,
        "metadata_relatedItems_resourceTypeGeneral": facets.metadata_relatedItems_resourceTypeGeneral,
        "metadata_relatedItems_schemeType": facets.metadata_relatedItems_schemeType,
        "metadata_relatedItems_schemeURI": facets.metadata_relatedItems_schemeURI,
        "metadata_relatedItems_titles_lang": facets.metadata_relatedItems_titles_lang,
        "metadata_relatedItems_titles_titleType": facets.metadata_relatedItems_titles_titleType,
        "metadata_relatedItems_volume": facets.metadata_relatedItems_volume,
        "metadata_rightsList_lang": facets.metadata_rightsList_lang,
        "metadata_rightsList_rights": facets.metadata_rightsList_rights,
        "metadata_rightsList_rightsIdentifier": facets.metadata_rightsList_rightsIdentifier,
        "metadata_rightsList_rightsIdentifierScheme": facets.metadata_rightsList_rightsIdentifierScheme,
        "metadata_rightsList_rightsURI": facets.metadata_rightsList_rightsURI,
        "metadata_rightsList_schemeURI": facets.metadata_rightsList_schemeURI,
        "metadata_schemaVersion": facets.metadata_schemaVersion,
        "metadata_sizes": facets.metadata_sizes,
        "metadata_subjects_classificationCode": facets.metadata_subjects_classificationCode,
        "metadata_subjects_lang": facets.metadata_subjects_lang,
        "metadata_subjects_schemeURI": facets.metadata_subjects_schemeURI,
        "metadata_subjects_subject": facets.metadata_subjects_subject,
        "metadata_subjects_subjectScheme": facets.metadata_subjects_subjectScheme,
        "metadata_subjects_valueURI": facets.metadata_subjects_valueURI,
        "metadata_titles_lang": facets.metadata_titles_lang,
        "metadata_titles_titleType": facets.metadata_titles_titleType,
        "metadata_types_resourceType": facets.metadata_types_resourceType,
        "metadata_types_resourceTypeGeneral": facets.metadata_types_resourceTypeGeneral,
        "metadata_url": facets.metadata_url,
        "metadata_version": facets.metadata_version,
        "oai_harvest_datestamp": facets.oai_harvest_datestamp,
        "oai_harvest_identifier": facets.oai_harvest_identifier,
        **getattr(InvenioSearchOptions, "facets", {}),
    }
