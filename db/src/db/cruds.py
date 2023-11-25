import uuid
from typing import Dict, List, Optional

from sqlalchemy.orm import Session
from src.db import models, schemas

# すべてのプロジェクトを選択
def select_project_all(db: Session) -> List[schemas.Project]:
    return db.query(models.Project).all()

# IDによってプロジェクトを選択
def select_project_by_id(
    db: Session,
    project_id: str,
) -> schemas.Project:
    return db.query(models.Project).filter(models.Project.project_id == project_id).first()

# 名前によってプロジェクトを選択
def select_project_by_name(
    db: Session,
    project_name: str,
) -> schemas.Project:
    return db.query(models.Project).filter(models.Project.project_name == project_name).first()

# プロジェクトを追加
def add_project(
    db: Session,
    project_name: str,
    description: Optional[str] = None,
    commit: bool = True,
) -> schemas.Project:
    exists = select_project_by_name(
        db=db,
        project_name=project_name,
    )
    if exists:
        return exists
    else:
        project_id = str(uuid.uuid4())[:6]
        data = models.Project(
            project_id=project_id,
            project_name=project_name,
            description=description,
        )
        db.add(data)
        if commit:
            db.commit()
            db.refresh(data)
        return data

# すべてのモデルを選択
def select_model_all(db: Session) -> List[schemas.Model]:
    return db.query(models.Model).all()

# IDによってモデルを選択
def select_model_by_id(
    db: Session,
    model_id: str,
) -> schemas.Model:
    return db.query(models.Model).filter(models.Model.model_id == model_id).first()

# プロジェクトIDによってモデルを選択
def select_model_by_project_id(
    db: Session,
    project_id: str,
) -> List[schemas.Model]:
    return db.query(models.Model).filter(models.Model.project_id == project_id).all()

# プロジェクト名によってモデルを選択
def select_model_by_project_name(
    db: Session,
    project_name: str,
) -> List[schemas.Model]:
    project = select_project_by_name(
        db=db,
        project_name=project_name,
    )
    return db.query(models.Model).filter(models.Model.project_id == project.project_id).all()

# 指定されたモデル名に基づいてモデルを選択します。
def select_model_by_name(
    db: Session,
    model_name: str,
) -> List[schemas.Model]:
    return db.query(models.Model).filter(models.Model.model_name == model_name).all()

# 新しいモデルを追加します。
def add_model(
    db: Session,
    project_id: str,
    model_name: str,
    parent_model_id: str =None,
    description: Optional[str] = None,
    commit: bool = True,
) -> schemas.Model:
    models_in_project = select_model_by_project_id(
        db=db,
        project_id=project_id,
    )
    # 同じ名前のモデルがすでにあるか確認します。
    for model in models_in_project:
        if model.model_name == model_name:
            return model
    model_id = str(uuid.uuid4())[:6]
    # モデルデータを作成します。
    data = models.Model(
        parent_model_id=parent_model_id,
        model_id=model_id,
        project_id=project_id,
        model_name=model_name,
        description=description,
    )
    db.add(data)
    if commit:
        db.commit()
        db.refresh(data)
    return data

# すべての実験を選択します。
def select_experiment_all(db: Session) -> List[schemas.Experiment]:
    return db.query(models.Experiment).all()

# 指定されたIDに基づいて実験を選択します。
def select_experiment_by_id(
    db: Session,
    experiment_id: str,
) -> schemas.Experiment:
    return db.query(models.Experiment).filter(models.Experiment.experiment_id == experiment_id).first()

# 指定されたモデルバージョンIDに基づいて実験を選択します。
def select_experiment_by_model_version_id(
    db: Session,
    model_version_id: str,
) -> schemas.Experiment:
    return db.query(models.Experiment).filter(models.Experiment.model_version_id == model_version_id).first()

# 指定されたモデルIDに基づいて実験を選択します。
def select_experiment_by_model_id(
    db: Session,
    model_id: str,
) -> List[schemas.Experiment]:
    return db.query(models.Experiment).filter(models.Experiment.model_id == model_id).all()

# 指定されたプロジェクトIDに基づいて実験を選択します。
def select_experiment_by_project_id(
    db: Session,
    project_id: str,
) -> List[schemas.Experiment]:
    return (
        db.query(models.Experiment, models.Model)
        .filter(models.Model.project_id == project_id)
        .filter(models.Experiment.model_id == models.Model.model_id)
        .all()
    )

# 新しい実験を追加します。
def add_experiment(
    db: Session,
    model_version_id: str,
    model_id: str,
    parameters: Optional[Dict] = None,
    training_dataset_path: Optional[str] = None,
    validation_dataset_path: Optional[str] = None,
    test_dataset_path: Optional[str] = None,
    evaluations: Optional[Dict] = None,
    artifact_file_paths: Optional[Dict] = None,
    commit: bool = True,
) -> schemas.Experiment:
    experiment_id = str(uuid.uuid4())[:6]
    # 実験データを作成します。
    data = models.Experiment(
        experiment_id=experiment_id,
        model_version_id=model_version_id,
        model_id=model_id,
        parameters=parameters,
        training_dataset_path=training_dataset_path,
        validation_dataset_path=validation_dataset_path,
        test_dataset_path=test_dataset_path,
        evaluations=evaluations,
        artifact_file_paths=artifact_file_paths,
    )
    db.add(data)
    if commit:
        db.commit()
        db.refresh(data)
    return data

# 実験の評価情報を更新します。
def update_experiment_evaluation(
    db: Session,
    experiment_id: str,
    evaluations: Dict,
) -> schemas.Experiment:
    data = select_experiment_by_id(
        db=db,
        experiment_id=experiment_id,
    )
    # 評価情報がない場合は新規作成、ある場合は更新します。
    if data.evaluations is None:
        data.evaluations = evaluations
    else:
        for k, v in evaluations.items():
            data.evaluations[k] = v
    db.commit()
    db.refresh(data)
    return data

# 実験の成果物ファイルパスを更新します。
def update_experiment_artifact_file_paths(
    db: Session,
    experiment_id: str,
    artifact_file_paths: Dict,
) -> schemas.Experiment:
    data = select_experiment_by_id(
        db=db,
        experiment_id=experiment_id,
    )
    # 成果物ファイルパスがない場合は新規作成、ある場合は更新します。
    if data.artifact_file_paths is None:
        data.artifact_file_paths = artifact_file_paths
    else:
        for k, v in artifact_file_paths.items():
            data.artifact_file_paths[k] = v
    db.commit()
    db.refresh(data)
    return data
