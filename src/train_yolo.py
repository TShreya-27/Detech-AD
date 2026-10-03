from ultralytics import YOLO
import torch


def main():

    # --------------------------------------------------
    # 2. Load pretrained YOLO26 Nano
    # --------------------------------------------------
    model = YOLO("yolo26n.pt")

    # --------------------------------------------------
    # 3. Train on TOI dataset
    # --------------------------------------------------
    model.train(
        data="configs/data.yaml",

        # Training
        epochs=1,
        imgsz=1280,
        batch=1,

        # Optimizer
        optimizer="auto",
        workers=0,
        # Early stopping
        patience=15,

        # Output
        project="runs",
        name="trained_yolo26n",
        exist_ok=True,

        # Save checkpoints
        save=True,
        save_period=5,

        # Validation
        val=True,

        # Reproducibility
        seed=42,

        # Avoid excessive RAM usage
        cache=False,

        # Display detailed training information
        verbose=True,

        # Generate training plots
        plots=True,
    )

    print("\nTOI training completed.")
    print("Best model should be saved at:")
    print("runs/trained_yolo26n/weights/best.pt")


if __name__ == "__main__":
    main()