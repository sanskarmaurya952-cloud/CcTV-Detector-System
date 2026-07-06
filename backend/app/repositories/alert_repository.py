from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertRepository:

    @staticmethod
    def create(
        db: Session,
        camera_id: int,
        alert_type: str,
        image_path: str
    ):
        alert = Alert(
            camera_id=camera_id,
            alert_type=alert_type,
            image_path=image_path
        )

        db.add(alert)
        db.commit()
        db.refresh(alert)

        return alert

    @staticmethod
    def get_all(db: Session):
        return (
            db.query(Alert)
            .order_by(Alert.created_at.desc())
            .all()
        )

    @staticmethod
    def get_by_id(db: Session, alert_id: int):
        return (
            db.query(Alert)
            .filter(Alert.id == alert_id)
            .first()
        )

    @staticmethod
    def delete(db: Session, alert_id: int):
        alert = (
            db.query(Alert)
            .filter(Alert.id == alert_id)
            .first()
        )

        if not alert:
            return None

        db.delete(alert)
        db.commit()

        return alert