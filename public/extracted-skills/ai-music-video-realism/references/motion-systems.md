# Natural Body Movement Systems

## Why bodies break
Models lose kinematics when the prompt asks for too much action, the still is a tight crop, the motion plate framing does not match the still, or contradictory style words fight each other.

## Default path (most music videos)
1. Approve a full-body still, limbs unoccluded, even light.
2. Write start pose → one action → end pose.
3. Image-to-video, 4–8 seconds.
4. Inspect feet, hands, spine, eye line. Reject rubber or slide.
5. Only then generate the next shot from the same still pack.

## Motion-transfer path
1. Plate: real human doing the move at moderate speed, full body in frame, little displacement.
2. Identity still: same shot size as the plate.
3. Bind plate = motion, still = appearance.
4. Avoid extreme spins, tiny-footwork bursts, and cropped plates.

## 3D extract + re-shoot path
Use when choreography is already filmed and you need a new camera or wardrobe.
1. Extract 3D body / motion from the plate.
2. Re-path the camera in a 3D app. Do not confuse camera move with character move.
3. Render an untextured motion+camera plate.
4. Reference-to-video with the identity still + that plate + a prompt that names who is performing.

## Motion bible (reuse on every shot)
- Pace: slow / measured / driving (pick one)
- Posture: spine, shoulders, chin
- Arms: what they are allowed to do
- Head: when it turns to camera
- Emotion: one look
- Timing: action starts immediately or after N beats
- Forbidden: snaps, idle sway that ignores tempo, extra characters

## Dance-specific
- I2V only
- Neutral prep pose
- 2–3 motion adjectives
- 4–6s bursts, assemble in the NLE
- Generate 2–3 variations per beat
