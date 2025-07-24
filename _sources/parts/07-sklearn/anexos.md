# Anexos

## Argumento _scoring_

Para definir una métrica como una cadena en un argumentos _scoring_, usar alguna de las siguientes opciones:

| Cadena | Función | Comentario |
| --- | --- | --- |
| **Clasificación** | |  |
| _'accuracy'_ | `metrics.accuracy_score` |  |
| _'balanced_accuracy'_ | `metrics.balanced_accuracy_score` |  |
| _'top_k_accuracy'_ | `metrics.top_k_accuracy_score` |  |
| _'average_precision'_ | `metrics.average_precision_score` |  |
| _'neg_brier_score'_ | `metrics.brier_score_loss` |  |
| _'f1'_ | `metrics.f1_score` | Para _targets_ binarios |
| _'f1_micro'_ | `metrics.f1_score` | micro-promedio |
| _'f1_macro'_ | `metrics.f1_score` | macro-promedio |
| _'f1_weighted'_ | `metrics.f1_score` | promedio ponderado |
| _'f1_samples'_ | `metrics.f1_score` | Para muestra multietiquetas |
| _'neg_log_loss'_ | `metrics.log_loss` | Requiere sorporte de _predict_proba_ |
| _'precision'_ etc. | `metrics.precision_score` | Aplican los mismos sufijos que en _'f1'_ |
| _'recall'_ etc. | `metrics.recall_score` | Aplican los mismos sufijos que en _'f1'_ |
| _'jaccard'_ etc. | `metrics.jaccard_score`| Aplican los mismos sufijos que en _'f1'_ |
| _'roc_auc'_ | `metrics.roc_auc_score` |  |
| _'roc_auc_ovr'_ | `metrics.roc_auc_score` |  |
| _'roc_auc_ovo'_ | `metrics.roc_auc_score` |  |
| _'roc_auc_ovr_weighted'_ | `metrics.roc_auc_score` |  |
| _'roc_auc_ovo_weighted'_ | `metrics.roc_auc_score` |  |
| **_Clustering_** |  |  |
| _'adjusted_mutual_info_score'_ | `metrics.adjusted_mutual_info_score` |  |
| _'adjusted_rand_score'_ | `metrics.adjusted_rand_score` |  |
| _'completeness_score'_ | `metrics.completeness_score` |  |
| _'fowlkes_mallows_score'_ | `metrics.fowlkes_mallows_score` |  |
| _'homogeneity_score'_ | `metrics.homogeneity_score` |  |
| _'mutual_info_score'_ | `metrics.mutual_info_score` |  |
| _'normalized_mutual_info_score'_ | `metrics.normalized_mutual_info_score` |  |
| _'rand_score'_ | `metrics.rand_score` |  |
| _'v_measure_score'_ | `metrics.v_measure_score` |  |
| **Regresión** | |  |
| _'explained_variance'_ | `metrics.explained_variance_score` |  |
| _'max_error'_ | `metrics.max_error` |  |
| _'neg_mean_absolute_error'_ | `metrics.mean_absolute_error` |  |
| _'neg_mean_squared_error'_ | `metrics.mean_squared_error` |  |
| _'neg_root_mean_squared_error'_ | `metrics.mean_squared_error` |  |
| _'neg_mean_squared_log_error'_ | `metrics.mean_squared_log_error` |  |
| _'neg_median_absolute_error'_ | `metrics.median_absolute_error` |  |
| _'r2'_ | `metrics.r2_score` |  |
| _'neg_mean_poisson_deviance'_ | `metrics.mean_poisson_deviance` |  |
| _'neg_mean_gamma_deviance'_ | `metrics.mean_gamma_deviance` |  |
| _'neg_mean_absolute_percentage_error'_ | `metrics.mean_absolute_percentage_error` |
