# -*- coding: utf-8 -*-

# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.cloud.aiplatform_v1beta1.types import (
    accelerator_type as accelerator_type_v1beta1,
    annotation as annotation_v1beta1,
    annotation_spec as annotation_spec_v1beta1,
    artifact as artifact_v1beta1,
    batch_prediction_job as batch_prediction_job_v1beta1,
    completion_stats as completion_stats_v1beta1,
    context as context_v1beta1,
    custom_job as custom_job_v1beta1,
    data_item as data_item_v1beta1,
    data_labeling_job as data_labeling_job_v1beta1,
    dataset as dataset_v1beta1,
    dataset_service as dataset_service_v1beta1,
    deployed_index_ref as matching_engine_deployed_index_ref_v1beta1,
    deployed_model_ref as deployed_model_ref_v1beta1,
    deployment_resource_pool as deployment_resource_pool_v1beta1,
    deployment_resource_pool_service as deployment_resource_pool_service_v1beta1,
    encryption_spec as encryption_spec_v1beta1,
    endpoint as endpoint_v1beta1,
    endpoint_service as endpoint_service_v1beta1,
    entity_type as entity_type_v1beta1,
    env_var as env_var_v1beta1,
    event as event_v1beta1,
    execution as execution_v1beta1,
    explanation as explanation_v1beta1,
    explanation_metadata as explanation_metadata_v1beta1,
    feature as feature_v1beta1,
    feature_group as feature_group_v1beta1,
    feature_monitoring_stats as feature_monitoring_stats_v1beta1,
    feature_online_store as feature_online_store_v1beta1,
    feature_online_store_admin_service as feature_online_store_admin_service_v1beta1,
    feature_online_store_service as feature_online_store_service_v1beta1,
    feature_selector as feature_selector_v1beta1,
    feature_view as feature_view_v1beta1,
    feature_view_sync as feature_view_sync_v1beta1,
    featurestore as featurestore_v1beta1,
    featurestore_monitoring as featurestore_monitoring_v1beta1,
    featurestore_online_service as featurestore_online_service_v1beta1,
    featurestore_service as featurestore_service_v1beta1,
    index as index_v1beta1,
    index_endpoint as index_endpoint_v1beta1,
    hyperparameter_tuning_job as hyperparameter_tuning_job_v1beta1,
    io as io_v1beta1,
    index_service as index_service_v1beta1,
    job_service as job_service_v1beta1,
    job_state as job_state_v1beta1,
    lineage_subgraph as lineage_subgraph_v1beta1,
    machine_resources as machine_resources_v1beta1,
    manual_batch_tuning_parameters as manual_batch_tuning_parameters_v1beta1,
    match_service as match_service_v1beta1,
    metadata_schema as metadata_schema_v1beta1,
    metadata_service as metadata_service_v1beta1,
    metadata_store as metadata_store_v1beta1,
    model as model_v1beta1,
    model_evaluation as model_evaluation_v1beta1,
    model_evaluation_slice as model_evaluation_slice_v1beta1,
    model_deployment_monitoring_job as model_deployment_monitoring_job_v1beta1,
    model_garden_service as model_garden_service_v1beta1,
    model_service as model_service_v1beta1,
    model_monitoring as model_monitoring_v1beta1,
    operation as operation_v1beta1,
    persistent_resource as persistent_resource_v1beta1,
    persistent_resource_service as persistent_resource_service_v1beta1,
    pipeline_failure_policy as pipeline_failure_policy_v1beta1,
    pipeline_job as pipeline_job_v1beta1,
    pipeline_service as pipeline_service_v1beta1,
    pipeline_state as pipeline_state_v1beta1,
    prediction_service as prediction_service_v1beta1,
    publisher_model as publisher_model_v1beta1,
    service_networking as service_networking_v1beta1,
    schedule as schedule_v1beta1,
    schedule_service as schedule_service_v1beta1,
    specialist_pool as specialist_pool_v1beta1,
    specialist_pool_service as specialist_pool_service_v1beta1,
    study as study_v1beta1,
    tensorboard as tensorboard_v1beta1,
    tensorboard_data as tensorboard_data_v1beta1,
    tensorboard_experiment as tensorboard_experiment_v1beta1,
    tensorboard_run as tensorboard_run_v1beta1,
    tensorboard_service as tensorboard_service_v1beta1,
    tensorboard_time_series as tensorboard_time_series_v1beta1,
    training_pipeline as training_pipeline_v1beta1,
    types as types_v1beta1,
    vizier_service as vizier_service_v1beta1,
)
from google.cloud.aiplatform_v1.types import (
    accelerator_type as accelerator_type_v1,
    annotation as annotation_v1,
    annotation_spec as annotation_spec_v1,
    artifact as artifact_v1,
    batch_prediction_job as batch_prediction_job_v1,
    completion_stats as completion_stats_v1,
    context as context_v1,
    custom_job as custom_job_v1,
    data_item as data_item_v1,
    data_labeling_job as data_labeling_job_v1,
    dataset as dataset_v1,
    dataset_service as dataset_service_v1,
    deployed_index_ref as matching_engine_deployed_index_ref_v1,
    deployed_model_ref as deployed_model_ref_v1,
    encryption_spec as encryption_spec_v1,
    endpoint as endpoint_v1,
    endpoint_service as endpoint_service_v1,
    entity_type as entity_type_v1,
    env_var as env_var_v1,
    event as event_v1,
    execution as execution_v1,
    explanation as explanation_v1,
    explanation_metadata as explanation_metadata_v1,
    feature as feature_v1,
    feature_group as feature_group_v1,
    feature_monitoring_stats as feature_monitoring_stats_v1,
    feature_online_store as feature_online_store_v1,
    feature_online_store_admin_service as feature_online_store_admin_service_v1,
    feature_online_store_service as feature_online_store_service_v1,
    feature_selector as feature_selector_v1,
    feature_view as feature_view_v1,
    feature_view_sync as feature_view_sync_v1,
    featurestore as featurestore_v1,
    featurestore_online_service as featurestore_online_service_v1,
    featurestore_service as featurestore_service_v1,
    hyperparameter_tuning_job as hyperparameter_tuning_job_v1,
    index as index_v1,
    index_endpoint as index_endpoint_v1,
    index_service as index_service_v1,
    io as io_v1,
    job_service as job_service_v1,
    job_state as job_state_v1,
    lineage_subgraph as lineage_subgraph_v1,
    machine_resources as machine_resources_v1,
    manual_batch_tuning_parameters as manual_batch_tuning_parameters_v1,
    metadata_service as metadata_service_v1,
    metadata_schema as metadata_schema_v1,
    metadata_store as metadata_store_v1,
    model as model_v1,
    model_evaluation as model_evaluation_v1,
    model_evaluation_slice as model_evaluation_slice_v1,
    model_deployment_monitoring_job as model_deployment_monitoring_job_v1,
    model_service as model_service_v1,
    model_monitoring as model_monitoring_v1,
    operation as operation_v1,
    pipeline_failure_policy as pipeline_failure_policy_v1,
    pipeline_job as pipeline_job_v1,
    pipeline_service as pipeline_service_v1,
    pipeline_state as pipeline_state_v1,
    prediction_service as prediction_service_v1,
    publisher_model as publisher_model_v1,
    schedule as schedule_v1,
    schedule_service as schedule_service_v1,
    service_networking as service_networking_v1,
    specialist_pool as specialist_pool_v1,
    specialist_pool_service as specialist_pool_service_v1,
    study as study_v1,
    tensorboard as tensorboard_v1,
    tensorboard_data as tensorboard_data_v1,
    tensorboard_experiment as tensorboard_experiment_v1,
    tensorboard_run as tensorboard_run_v1,
    tensorboard_service as tensorboard_service_v1,
    tensorboard_time_series as tensorboard_time_series_v1,
    training_pipeline as training_pipeline_v1,
    types as types_v1,
    vizier_service as vizier_service_v1,
)

__all__ = (
    # v1
    accelerator_type_v1,
    annotation_v1,
    annotation_spec_v1,
    artifact_v1,
    batch_prediction_job_v1,
    completion_stats_v1,
    context_v1,
    custom_job_v1,
    data_item_v1,
    data_labeling_job_v1,
    dataset_v1,
    dataset_service_v1,
    deployed_model_ref_v1,
    encryption_spec_v1,
    endpoint_v1,
    endpoint_service_v1,
    entity_type_v1,
    env_var_v1,
    event_v1,
    execution_v1,
    explanation_v1,
    explanation_metadata_v1,
    feature_v1,
    feature_monitoring_stats_v1,
    feature_selector_v1,
    featurestore_v1,
    featurestore_online_service_v1,
    featurestore_service_v1,
    hyperparameter_tuning_job_v1,
    io_v1,
    job_service_v1,
    job_state_v1,
    lineage_subgraph_v1,
    machine_resources_v1,
    manual_batch_tuning_parameters_v1,
    matching_engine_deployed_index_ref_v1,
    index_v1,
    index_endpoint_v1,
    index_service_v1,
    metadata_service_v1,
    metadata_schema_v1,
    metadata_store_v1,
    model_v1,
    model_evaluation_v1,
    model_evaluation_slice_v1,
    model_deployment_monitoring_job_v1,
    model_service_v1,
    model_monitoring_v1,
    operation_v1,
    persistent_resource_v1beta1,
    pipeline_failure_policy_v1,
    pipeline_job_v1,
    pipeline_service_v1,
    pipeline_state_v1,
    prediction_service_v1,
    publisher_model_v1,
    schedule_v1,
    schedule_service_v1,
    specialist_pool_v1,
    specialist_pool_service_v1,
    tensorboard_v1,
    tensorboard_data_v1,
    tensorboard_experiment_v1,
    tensorboard_run_v1,
    tensorboard_service_v1,
    tensorboard_time_series_v1,
    training_pipeline_v1,
    types_v1,
    study_v1,
    vizier_service_v1,
    # v1beta1
    accelerator_type_v1beta1,
    annotation_v1beta1,
    annotation_spec_v1beta1,
    artifact_v1beta1,
    batch_prediction_job_v1beta1,
    completion_stats_v1beta1,
    context_v1beta1,
    custom_job_v1beta1,
    data_item_v1beta1,
    data_labeling_job_v1beta1,
    dataset_v1beta1,
    dataset_service_v1beta1,
    deployment_resource_pool_v1beta1,
    deployment_resource_pool_service_v1beta1,
    deployed_model_ref_v1beta1,
    encryption_spec_v1beta1,
    endpoint_v1beta1,
    endpoint_service_v1beta1,
    entity_type_v1beta1,
    env_var_v1beta1,
    event_v1beta1,
    execution_v1beta1,
    explanation_v1beta1,
    explanation_metadata_v1beta1,
    feature_v1beta1,
    feature_monitoring_stats_v1beta1,
    feature_selector_v1beta1,
    featurestore_v1beta1,
    featurestore_monitoring_v1beta1,
    featurestore_online_service_v1beta1,
    featurestore_service_v1beta1,
    hyperparameter_tuning_job_v1beta1,
    io_v1beta1,
    job_service_v1beta1,
    job_state_v1beta1,
    lineage_subgraph_v1beta1,
    machine_resources_v1beta1,
    manual_batch_tuning_parameters_v1beta1,
    matching_engine_deployed_index_ref_v1beta1,
    index_v1beta1,
    index_endpoint_v1beta1,
    index_service_v1beta1,
    match_service_v1beta1,
    metadata_service_v1beta1,
    metadata_schema_v1beta1,
    metadata_store_v1beta1,
    model_v1beta1,
    model_evaluation_v1beta1,
    model_evaluation_slice_v1beta1,
    model_deployment_monitoring_job_v1beta1,
    model_garden_service_v1beta1,
    model_service_v1beta1,
    model_monitoring_v1beta1,
    operation_v1beta1,
    pipeline_failure_policy_v1beta1,
    pipeline_job_v1beta1,
    pipeline_service_v1beta1,
    pipeline_state_v1beta1,
    prediction_service_v1beta1,
    publisher_model_v1beta1,
    schedule_v1beta1,
    schedule_service_v1beta1,
    specialist_pool_v1beta1,
    specialist_pool_service_v1beta1,
    study_v1beta1,
    tensorboard_v1beta1,
    tensorboard_data_v1beta1,
    tensorboard_experiment_v1beta1,
    tensorboard_run_v1beta1,
    tensorboard_service_v1beta1,
    tensorboard_time_series_v1beta1,
    training_pipeline_v1beta1,
    types_v1beta1,
    vizier_service_v1beta1,
)
