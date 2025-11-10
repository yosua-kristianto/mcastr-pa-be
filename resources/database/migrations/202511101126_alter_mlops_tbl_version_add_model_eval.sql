ALTER TABLE mlops_tbl_version
ADD COLUMN `eval_score` FLOAT AFTER `model_name`,
ADD COLUMN `report` BLOB AFTER `eval_score`
;