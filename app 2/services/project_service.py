import datetime
import re

from sqlalchemy import func

from .. import db
from ..models.project_model import Project

from ..models.sentence_model import Sentence
from ..schemas.project_schema import project_schema, projects_schema


def create_project(data, current_user):
    new_project = Project(
        title=data['title'],
        description=data['description'],
        language=data['language'],
        file_text=data['file_text'],
        uploaded_by=current_user,
        uploaded_on=datetime.datetime.now()
    )

    db.session.add(new_project)
    db.session.flush()
    sentences = split_into_sentences(data['file_text'])
    for sentence_text in sentences:
        sentence = Sentence(content=sentence_text.strip(), project_id=new_project.id, is_annotated=False)
        db.session.add(sentence)

    db.session.commit()
    return new_project


def split_into_sentences(text):
    if not text:
        return []

    # Split the text by full stop or '|', filter out any empty sentences
    sentences = [s.strip() for s in re.split(r'[.|।]', text) if s.strip()]
    return sentences


def get_projects_by_language(language):
    project = Project.query.filter_by(language=language).order_by(Project.id .desc()).all()
    return project


def get_projects():
    project = Project.query.filter_by().order_by(Project.id.desc()).all()
    return project



def get_projects_with_annotation_counts():
    # Subquery to count annotated sentences for each project
    annotated_subquery, unannotated_subquery = get_annotation_subquery()
    # Main query to get projects with annotated and unannotated counts
    projects = db.session.query(
        Project,
        func.coalesce(annotated_subquery.c.annotated_count, 0).label('annotated_sentences'),
        func.coalesce(unannotated_subquery.c.unannotated_count, 0).label('unannotated_sentences')
    ).outerjoin(
        annotated_subquery, Project.id == annotated_subquery.c.project_id
    ).outerjoin(
        unannotated_subquery, Project.id == unannotated_subquery.c.project_id
    ).order_by(Project.id.desc()).all()  # Note the correction here
    return projects


def get_projects_with_annotation_counts_with_language(language):
    # Subquery to count annotated sentences for each project
    annotated_subquery, unannotated_subquery = get_annotation_subquery()
    # Main query to get projects with annotated and unannotated counts
    projects = db.session.query(
        Project,
        func.coalesce(annotated_subquery.c.annotated_count, 0).label('annotated_sentences'),
        func.coalesce(unannotated_subquery.c.unannotated_count, 0).label('unannotated_sentences')
    ).outerjoin(
        annotated_subquery, Project.id == annotated_subquery.c.project_id
    ).outerjoin(
        unannotated_subquery, Project.id == unannotated_subquery.c.project_id
    ).filter(Project.language == language).order_by(Project.id.desc()).all()  # Note the correction here
    return projects

def get_annotation_subquery():
    annotated_subquery = db.session.query(
        Sentence.project_id,
        func.count('*').label('annotated_count')
    ).filter_by(is_annotated=True).group_by(Sentence.project_id).subquery()

    # Subquery to count unannotated sentences for each project
    unannotated_subquery = db.session.query(
        Sentence.project_id,
        func.count('*').label('unannotated_count')
    ).filter_by(is_annotated=False).group_by(Sentence.project_id).subquery()
    return annotated_subquery, unannotated_subquery