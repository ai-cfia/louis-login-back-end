from datetime import datetime, timedelta
import jwt

def generate_jwt(data, priv_key):
    """
    Generate a JWT using the given data and private key.
    """
    # Set the expiration time for the JWT
    data['exp'] = datetime.utcnow() + timedelta(hours=1)  # JWT expires in 1 hour

    # Create the JWT using the RS256 algorithm
    jwt_token = jwt.encode(data, priv_key, algorithm='RS256')

    return jwt_token

if __name__ == "__main__":
    # Load the private key
    with open('keys/private_key.pem', 'rb') as f:
        private_key_content = f.read()

    # Sample data with a redirect_url
    sample_data = {
        "redirect_url": "https://www.google.com/"
    }

    # Generate the JWT
    GENERATED_JWT = generate_jwt(sample_data, private_key_content)
    print(f"Generated JWT: {GENERATED_JWT}")
