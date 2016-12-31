from flask import Blueprint, flash, redirect, render_template, url_for

import projectile

from . import forms
from .project import Project


blueprint = Blueprint('projectile', __name__)


@blueprint.route("/")
def home():
    create_form = forms.CreateProjectForm()
    return render_template('home.html', create_form=create_form)


@blueprint.route('/projet/creer', methods=['POST'])
def create_project():
    form = forms.CreateProjectForm()

    if not form.validate_on_submit():
        flash('Merci de fournir une url.', 'error')
        return redirect(url_for('projectile.home'))

    project = Project(form.url.data)
    
    # Check if the project manager is on the card
    if not project.is_project_manager_on_card():
        flash(
            "Tu n'es pas sur la tuile Trello. Merci de demander au DC de t'ajouter.",
            "error"
        )
        return redirect(url_for('projectile.home'))

    # Create the folder locally
    try:
        project.create_folder()
    except projectile.project.ProjectExistsError:
        flash("Une étude porte déjà ce nom. Merci de renommer la tuile Trello.", "error")
        return redirect(url_for('projectile.home'))

    # Download the documents on GDrive
    project.downloader.download_documents()

    # Rename the database
    project.reader.configure_documents()

    # Add a quality member on the Trello card
    # Insert the Trello card in the right list
    project.design()

    # Create the GDrive folder
    project.uploader.create_folder(project.reader.get_odt_names())
        
    # Share the GDrive folder with the quality member
    project.uploader.share_folder(project.get_quality_member_mail())

    flash("L'étude a été créée avec succès.", 'success')
    return redirect(url_for('projectile.home'))
